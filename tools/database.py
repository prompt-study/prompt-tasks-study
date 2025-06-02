import os
import json
import csv
import asyncio
import shutil
import sqlite3
from tqdm import tqdm
from datetime import datetime
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
import sys
import random
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
# from run_sonarqube import SonarqubeReport
from sqlalchemy.sql import func
from sqlalchemy import inspect, create_engine, text, column, Column, Integer, Float, String, Text, Boolean, DateTime, LargeBinary, MetaData, Table, select, bindparam, literal
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoSuchTableError, IntegrityError
import hashlib
import sys
import re
import sqlalchemy
import pytz 
from pympler import asizeof
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import time
import traceback





sys.setrecursionlimit(2000)


class Database:
    def __init__(self, db_local_path=None):
        try:
            prefix = "/mnt/my_ssd/research"
            relative_path = os.path.relpath(db_local_path, start="/home/enio/projects/research")
            self.hardcoded_path = os.path.join(prefix, relative_path).replace('new_adr_study.db', 'adr_study.db')

        except Exception as e: 
            print(f'{e}')
            self.hardcoded_path = None
            
        self.db_local_path = db_local_path
        if self.db_local_path and os.path.exists(self.db_local_path):
            try:
                # Try to connect and execute a simple query
                test_engine = create_engine(f'sqlite:///{self.db_local_path}')
                with test_engine.connect() as conn:
                    conn.execute(text("SELECT 1"))
                    
            except sqlalchemy.exc.DatabaseError as e:
                if 'database disk image is malformed' in str(e):
                    print(f"Database at {self.db_local_path} is malformed. Deleting corrupted database.")
                    os.remove(self.db_local_path)
                    # if os.path.exists(self.hardcoded_path):
                    #     try:    
                    #         test_engine = create_engine(f'sqlite:///{self.hardcoded_path}')
                    #         with test_engine.connect() as conn:
                    #             conn.execute(text("SELECT 1"))
                            
                    #     except sqlalchemy.exc.DatabaseError as e:
                    #         if 'database backup disk image is malformed' in str(e):
                    #             os.remove(self.hardcoded_path)
                                
                    #         else:
                    #             raise  # Re-raise exception if it's a different error
                            
                    #     shutil.copy(self.hardcoded_path, self.db_local_path)
                    #     # self.engine.dispose()
                    #     # self.engine = create_engine(f'sqlite:///{self.db_local_path}')
                    #     # self.session = self.Session(bind=self.engine)
                    #     print(f"Database copied from {self.hardcoded_path} to {self.db_local_path}.")
                    # else:
                    #     print(f"No backup database found at {self.hardcoded_path}. A new database will be initialized.")
                else:
                    raise  # Re-raise exception if it's a different error
                
        if os.path.exists(self.hardcoded_path):
            if not 'new_' in self.db_local_path.replace('new_adr_study.db', 'adr_study.db'):
                shutil.copy(self.hardcoded_path, self.db_local_path.replace('new_adr_study.db', 'adr_study.db'))
                # print(f"Database copied from {self.hardcoded_path} to {self.db_local_path}.")
                try:
                    os.remove(self.hardcoded_path) 
                    # print(f"OLD DB PURGED, NOW WE ARE ON OUR OWN {self.hardcoded_path}.")
                except:
                    pass    
            else:
                print(f"No database found at {self.hardcoded_path}. A new database will be initialized.")

        db_url = "postgresql://postgres:Scnmhf-8950@home:5432/your_db"
        self.engine = create_engine(db_url) if db_local_path is None else create_engine(f'sqlite:///{self.db_local_path}')
        self.metadata = MetaData()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.data = []
        self.table_name = None

    def get_hashline(self, value):
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def get_hashlines_done(self, table_name='adr_metrics'):
        if not self.table_exists(table_name):
            # print(f"Table '{table_name}' does not exist.")
            return set()
        table = Table(table_name, self.metadata, autoload_with=self.engine)
        stmt = select(table.c.hashline)
        result = self.session.execute(stmt).fetchall()
        hashes = {row[0] for row in result}
        # print(f"Fetched {len(hashes)} processed hashes from '{table_name}'")
        return list(hashes)
    
    
    def execute_sql(self, query: str) -> list | None:
        with self.engine.connect() as conn:
            result = conn.execute(text(query))
            if result.returns_rows:
                return result.fetchall()
            conn.commit()
            return None

    def cache(self, item, table_name):
        self.data.append((item, table_name))
        item_memory = asizeof.asizeof(self.data)
        # print(f'ITEM MEMORY: {item_memory}')
        if item_memory >= 1e6 or len(self.data) > 70:
            # print(f'SAVE: {item_memory}')
            self.save()
            
    def backup_database(self, clean_local=False):
        """
        Perform the database backup operation.
        If a stop signal is received, terminate the operation gracefully.
        """
        
        if self.backup_in_progress.is_set():
            print("Backup in progress. Attempting to stop the current backup...")
            self.stop_backup.set()  # Signal the current backup to stop
            self.backup_in_progress.clear()  # Clear the in-progress flag

        with self.save_lock:  # Ensure this operation is thread-safe
            self.backup_in_progress.set()  # Mark backup as in progress
            self.stop_backup.clear()  # Clear stop signal

            try:
                print("Starting backup operation...")
                backup_path = self.hardcoded_path
                if self.db_local_path:
                    shutil.copy(self.db_local_path, backup_path)  # Copy the database file
                    print(f"Database backup completed to {backup_path}.")
                    if clean_local:
                        print(f'WARNING: Clean local passed as True. be careful!')
                        os.remove(self.db_local_path)
                else:
                    print("No local database to back up.")
            except Exception as e:
                print(f"Backup failed: {e}")
            finally:
                self.backup_in_progress.clear()  # Mark backup as no longer in progress
                print("Backup operation finished.")

    def save(self):
        number_retries = 5
        wait_time = 0.0
        group = {}
        if len(self.data) == 0:
            return False
        
        for idx, (data, table_name) in enumerate(self.data):
            
            if table_name not in group:
                group[table_name] = []
                
            if isinstance(data, list):
                data = [data_ for data_ in data if len(data_) !=0 and isinstance(data_, dict)]
                group[table_name].extend(data)
                
            elif isinstance(data, pd.DataFrame):
                converted = data.to_dict(orient='records')
                group[table_name].extend(converted)
                
            elif isinstance(data, dict):    
                if len(data) !=0:
                    group[table_name].append(data)
                    
            elif data is None:
                continue
            else:
                raise Exception(f'Saved data not according to necessary data types: {type(data)} from data\n{data}')
        saved = False
        for attempt in range(1, number_retries + 1):
            if saved:
                break
            if wait_time > 0:
                time.sleep(wait_time)
                
            with self.engine.connect() as conn:
                try:
                    for table_idx, (table_name, values) in enumerate(group.items()):
                        if len(values) == 0:
                            continue
                        
                        _table_cache = {}
                        try:
                            insp = inspect(conn)
                            columns = [col['name'] for col in insp.get_columns(table_name)]
                            _table_cache[table_name] = {
                                'columns': columns,
                                'insert_sql': self._prepare_insert_sql(table_name, columns)
                            }
                        except Exception as e:
                            print(f"!! Failed to reflect table '{table_name}': {str(e)}")
                            traceback.print_exc()
                            raise

                        cache = _table_cache[table_name]
                        insert_sql = cache['insert_sql']
                        columns = cache['columns']
                        max_params = 999
                        chunk_size = max_params // len(columns) if columns else 0
                        if chunk_size == 0:
                            print("!! Warning: Zero chunk size - possible missing columns reflection")

                        total_chunks = (len(values) + chunk_size - 1) // chunk_size if chunk_size else 1
                        for i in range(0, len(values), chunk_size):
                            chunk = values[i:i+chunk_size]
                            
                            params = []
                            for item in chunk:
                                filtered = {k: v for k, v in item.items() if k in columns}
                                if len(filtered) != len(item):
                                    missing = set(item.keys()) - set(filtered.keys())
                                    print(f"!! Warning: Filtered out keys {missing} not in table columns")
                                params.append(filtered)
                            
                            
                            try:
                                self._execute_batch(conn, insert_sql, params)
                                
                            except Exception as e:
                                print(f"!! Failed to execute chunk: {str(e)}")
                                print(f"!! Problematic SQL: {insert_sql}")
                                raise

                    conn.commit()
                    saved = True
                    break
                
                except Exception as e:
                    print("\n!! Exception occurred during save operation")
                    print(f"!! Error: {str(e)}")
                    print("Performing rollback")
                    conn.rollback()
                    additional_delay = random.uniform(1, 3)
                    wait_time += additional_delay
                    print(f"Incrementing wait time by {additional_delay:.2f} seconds (total: {wait_time:.2f} seconds).")
        

        self.data = []
        return saved
    
    def _prepare_insert_sql(self, table_name, columns):

        cols = ', '.join(columns)
        placeholders = ', '.join([f':{col}' for col in columns])
        return text(f"""
                INSERT OR REPLACE INTO {table_name}
                ({cols})
                VALUES ({placeholders})
            """)

    def _execute_batch(self, conn, statement, params):
        """Helper for safe parameterized batch execution"""
        conn.execute(statement, params)
    
    def table_exists(self, table_name):
        inspector = inspect(self.engine)
        return table_name in inspector.get_table_names()

    def list_tables(self):
        inspector = inspect(self.engine)
        return inspector.get_table_names()
    
    def drop_table(self, table_name):
        if self.table_exists(table_name):
            table = Table(table_name, self.metadata, autoload_with=self.engine)
            table.drop(self.engine)
            self.session.commit()
            print(f"Table '{table_name}' dropped.")
        else:
            print(f"Table '{table_name}' does not exist and cannot be dropped.")

    def export_data(self, table_name):
        if not self.table_exists(table_name):
            # print(f"Table '{table_name}' does not exist.")
            return []
        table = Table(table_name, self.metadata, autoload_with=self.engine)
        rows = self.session.execute(table.select()).fetchall()
        return [dict(row._mapping) for row in rows]

    def import_data(self, data, table_name):
        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient='records')
        for row in data:
            self.cache(row, table_name=table_name)
        self.save()
        return self.save()
    
    def receive_sync(self, remote_db, local_table_name):
        local_table_name
        remote_tables = remote_db.list_tables()
        tables = [remote_table for remote_table in remote_tables if local_table_name in remote_tables]

        data = remote_db.export_data(local_table_name)
        if data:
            self.import_data(data, local_table_name)
            self.save()
            
    def sync_dir_with_main(self):
        base_path = os.path.dirname(self.db_local_path)
        prefix = "/mnt/my_ssd/research/adrs/datasets/project_repositories"
        # print(f'synching from {base_path}')
        table_names = ['commiter_metrics', 'developer_metrics']
        for table in table_names:
            data_cached = []
            print(f'synching table: {table}')
            for dirname in os.listdir(base_path):
                if os.path.isdir(os.path.join(base_path, dirname)):
                    for second_dirname in os.listdir(os.path.join(base_path, dirname)):
                        if second_dirname.endswith('adr_study.db'):
                            filepath = os.path.join(base_path, dirname, second_dirname)
                            try: 
                                print(f'instantiating')
                                remote_db = Database(filepath)
                                print(f'exporting')
                                data_cached += remote_db.export_data(table)
                            except Exception as e:
                                print(f'except: {e}')
        self.import_data(data_cached, 'metrics')
        self.save()
                            
                            
    def _define_table(self, table_name, item):
        columns = [Column('hashline', String, primary_key=True)]
        for key, value in item.items():
            if key != 'hashline':
                columns.append(Column(key, self._get_sql_type(value)))
        Table(table_name, self.metadata, *columns)
        self.metadata.create_all(self.engine)
        # print(f"Defined new table '{table_name}' with columns: {[col.name for col in columns]}")

    def _get_sql_type(self, value):
        if isinstance(value, int):
            return Integer
        elif isinstance(value, float):
            return Float
        elif isinstance(value, str):
            return String
        elif isinstance(value, bool):
            return Boolean
        elif isinstance(value, DateTime):
            return DateTime
        return String

    def get_viable_tablename(self, table_name):
        return re.sub(r'[^A-Za-z0-9_]+', '_', table_name[-60:])
    
    def get_steps_tag(self, raw_info_self_steps, mode, raw_info_self_substeps):
    
        new_step_id = mode + '_-_' + str(raw_info_self_steps)
        for self_substep in sorted(list(raw_info_self_substeps)):
            new_step_id = new_step_id + '_-_' + str(self_substep)
                
        return new_step_id       
    
    def unify_steps(self, new_routine_name, mode, table_name):
        
        cached = 0
        raw_info_list = []
        distinguishing_parts = {
            'create_metrics': ['create_metrics', 'create_metr/ics'],
            'extract_pydriller': ['extract_pydriller',],
            'adr_status_change': ['adr_status_change',],
            'adr_status_transition': ['adr_status_transition','calculate_status_transition'],
            'sonarqube_report': ['sonarqube_report',],
            'render_change_tree': ['render_change_tree',],
        }
        
        substep_distinguishing_parts = set()

        step_status_tables = self.list_tables()
        
        df_step_status = [self.to_df(step_status_table) for step_status_table in step_status_tables if 'status' in step_status_table]
        agg_df = pd.concat(df_step_status, ignore_index=True)
        for routine_name, group in agg_df.groupby('routine_name'):
            for index, row in group.iterrows():
                self_steps = set()
                self_substeps = set()
                for key, step in distinguishing_parts.items():
                    for step_variant in step:
                        if step_variant in row['step_id']:
                            self_steps.add(key)
                        
                if not self_steps:
                    continue 
                      
                if '_-_' in row['step_id']:
                    for substep in row['step_id'].split('_-_'):
                        try:
                            if int(substep) and int(substep) >= 1 and int(substep) <= 12:  # month substep
                                substep_distinguishing_parts.add(int(substep))
                                self_substeps.add(int(substep))
                                continue
                        except:
                            pass
                        
                        try:
                            if int(substep) and int(substep) >= 1900 and int(substep) <= 2030:  # year substep
                                substep_distinguishing_parts.add(int(substep))
                                self_substeps.add(int(substep))
                                continue
                        except:
                            pass
                        
                        try:
                            if str(substep) and '.md' in str(substep) or 'adr' in str(substep) or '.txt' in str(substep):  # adr substep
                                substep_distinguishing_parts.add(substep)
                                self_substeps.add(substep)
                                continue
                        except:
                            pass
                        
                        try:
                            if substep in substep_distinguishing_parts:
                                self_substeps.add(substep)
                                continue
                        except:
                            pass
                        
                if pd.isna(row['completed_at']):
                    continue
                
                self_info = {
                    'new_routine_name': new_routine_name,
                    'status': row['status'],
                    'step_id': row['step_id'],
                    'completed_date': row['completed_at'],
                    'self_steps': self_steps,
                    'self_substeps': self_substeps,
                    'mode': mode,
                }
                raw_info_list.append(self_info)
            
        for raw_info in raw_info_list:
            if raw_info['self_steps'] and len(raw_info['self_steps']) == 1:
                
                step_name = list(raw_info['self_steps'])[0]
                new_step_id = self.get_steps_tag(step_name, mode, raw_info['self_substeps'])
                
                    
                info_to_df = {
                    'mode': raw_info['mode'],
                    'routine_name': raw_info['new_routine_name'],
                    'status': raw_info['status'],
                    'step_id': new_step_id,
                    'completed_at': raw_info['completed_date'],
                }
                
                self.cache(info_to_df, table_name)
                cached += 1

            else:
                raise Exception(f"error regarding step nomenclature, here is the self_steps value = {raw_info['self_steps']} mode: {mode}")
        print(f'saving n {cached}')    
        self.save()

    def initialize_processing_steps(self, routine_name, total_steps, reset=False):
        try:
            table_name = self.get_viable_tablename(f"{routine_name}")
            print(f'this is the current tablename: {table_name}')
            if not reset and self.table_exists(table_name):
                print(f'enter?')
                expected_columns = {'mode', 'routine_name', 'step_id', 'status', 'completed_at'}
                inspector = inspect(self.engine)
                existing_columns = {col['name'] for col in inspector.get_columns(table_name)}
                
                if existing_columns != expected_columns:
                    print(f"Schema mismatch detected for table '{table_name}'. Resetting...")
                    # Re-call the function with reset=True to recreate the table
                    self.initialize_processing_steps(routine_name, total_steps, reset=True)
                    return table_name
                else:
                    # print(f"Table '{table_name}' already matches the expected schema.")
                    return table_name
            else:
                if self.table_exists(table_name):
                    self.metadata.remove(Table(table_name, self.metadata))
                    processing_table = Table(table_name, self.metadata, autoload_with=self.engine)
                    self.metadata.drop_all(self.engine, [processing_table])
                    self.metadata.remove(Table(table_name, self.metadata))
        
                # Create the table and initialize all steps
                processing_table = Table(
                    table_name, self.metadata,
                    
                    Column('mode', String, primary_key=True),
                    Column('routine_name', String, primary_key=True),
                    Column('step_id', String, primary_key=True),
                    Column('status', String, primary_key=True),
                    Column('completed_at', DateTime, primary_key=True),
                    extend_existing=True
                )
                self.metadata.create_all(self.engine)
                
                    # Insert all steps using OR IGNORE to avoid duplicates
                    # for step in range(1, total_steps + 1):
                    #     stmt = processing_table.insert().prefix_with("OR IGNORE").values(
                    #         routine_name=routine_name,
                    #         step_id=step,
                    #         status='pending',
                    #         completed_at=None
                    #     )
                    #     self.session.execute(stmt)
                self.session.commit()
                return table_name
            
        except sqlalchemy.exc.DatabaseError as e:
            if 'database disk image is malformed' in str(e):
                # print(f"Database at {self.db_local_path} is malformed. Deleting corrupted database.")
                os.remove(self.db_local_path)
                if os.path.exists(self.hardcoded_path):
                    shutil.copy(self.hardcoded_path, self.db_local_path)
                    print(f"Database at {self.db_local_path} is malformed. Database copied from {self.hardcoded_path} to {self.db_local_path}.")
                else:
                    print(f"Database at {self.db_local_path} is malformed. No backup database found at {self.hardcoded_path}. A new database will be initialized.")
                self.initialize_processing_steps(routine_name, total_steps, reset=True)
            else:
                raise  # Re-raise exception if it's a different error
        except Exception as e:
            print(f'this is whats happening: {e}')


    def get_step_status(self, routine_name, mode, step_id, date=None):
        table_name = routine_name
        try:
            processing_table = Table(table_name, self.metadata, autoload_with=self.engine)
        except NoSuchTableError:
            raise Exception(f"Table {table_name} does not exist. Please initialize it first.")
        
        except sqlalchemy.exc.DatabaseError as e:
            if 'database disk image is malformed' in str(e):
                # print(f"Database at {self.db_local_path} is malformed. Deleting corrupted database.")
                os.remove(self.db_local_path)
                if os.path.exists(self.hardcoded_path):
                    shutil.copy(self.hardcoded_path, self.db_local_path)
                    print(f"Database at {self.db_local_path} is malformed. Database copied from {self.hardcoded_path} to {self.db_local_path}.")
                else:
                    print(f"Database at {self.db_local_path} is malformed. No backup database found at {self.hardcoded_path}. A new database will be initialized.")
        try:
            processing_table = Table(table_name, self.metadata, autoload_with=self.engine)
        except NoSuchTableError:
            raise Exception(f"Table {table_name} does not exist. Please initialize it first.")
        # Combine conditions correctly using `&`
        if date is not None:
            stmt = processing_table.select().where(
                (processing_table.c.routine_name == routine_name) & 
                (processing_table.c.mode == mode) & 
                (processing_table.c.completed_at >= date) &
                (processing_table.c.step_id == step_id)
            )
        else:
            stmt = processing_table.select().where(
                (processing_table.c.routine_name == routine_name) & 
                (processing_table.c.mode == mode) & 
                (processing_table.c.step_id == step_id)
            )
            
        result = self.session.execute(stmt).fetchone()
        # print(f"get_step_status: DEBUG result type = {type(result)}, value = {result}")
        # print(f"get_step_status: DEBUG query values: routine_name = {routine_name}, mode = {mode}, step_id = {step_id}, date = {date}")
        if result:
            # Use ._mapping to access as a dictionary
            return result._mapping['status']
        else:
            return None

    def mark_step_complete(self, routine_name, mode, step_id):
        table_name = routine_name
        try:
            # Safely load the table schema
            processing_table = Table(table_name, self.metadata, autoload_with=self.engine)
        except NoSuchTableError:
            raise Exception(f"Table {table_name} does not exist. Please initialize it first.")
        except sqlalchemy.exc.DatabaseError as e:
            if 'database disk image is malformed' in str(e):
                # print(f"Database at {self.db_local_path} is malformed. Deleting corrupted database.")
                os.remove(self.db_local_path)
                if os.path.exists(self.hardcoded_path):
                    shutil.copy(self.hardcoded_path, self.db_local_path)
                    print(f"Database at {self.db_local_path} is malformed. Database copied from {self.hardcoded_path} to {self.db_local_path}.")
                else:
                    print(f"Database at {self.db_local_path} is malformed. No backup database found at {self.hardcoded_path}. A new database will be initialized.")
        try:
            # Safely load the table schema
            processing_table = Table(table_name, self.metadata, autoload_with=self.engine)
        except NoSuchTableError:
            raise Exception(f"Table {table_name} does not exist. Please initialize it first.")
        # Use INSERT OR REPLACE to either insert or update the row
        if 'test' in mode:
            status_sent = 'test cpl'
        else:
            status_sent = 'complete'
        stmt = processing_table.insert().prefix_with("OR REPLACE").values(
            routine_name=routine_name,
            step_id=step_id,
            status=status_sent,
            mode=mode,
            completed_at=func.now()
        )
        self.session.execute(stmt)
        self.session.commit()
        
    def sync(self, remote_db):
        tables = self.list_tables()
        for table_name in tables:
            try:
                data = self.export_data(table_name)
                if data:
                    remote_db.import_data(data, table_name)
            except Exception as e:
                print(f"Error transferring data from table '{table_name}': {e}")
    

    def get_hashlines_date_done(self, table_name='adr_metrics'):
        if not self.table_exists(table_name):
            # print(f"Table '{table_name}' does not exist.")
            return None
        table = Table(table_name, self.metadata, autoload_with=self.engine)
        stmt = select(func.max(table.c.author_date))  # Assuming 'author_date' is the column with the commit date
        result = self.session.execute(stmt).scalar()
        
        if result:
            # Ensure result is a datetime object, converting if necessary
            if isinstance(result, str):
                # Parse the string to a datetime object, assuming it’s in "YYYY-MM-DD HH:MM:SS" format
                result = datetime.strptime(result, "%Y-%m-%d %H:%M:%S")
            # Add UTC timezone
            return result.replace(tzinfo=pytz.UTC)
        else:
            # print("No previous commit date found; processing all commits.")
            return None
        
    def to_df(self, table_name, filter_dict=None, line_limit=None, randomize=False):
        if not self.table_exists(table_name):
            return pd.DataFrame()

        table = Table(table_name, self.metadata, autoload_with=self.engine)
        stmt = select(table)

        if filter_dict:
            for key, value in filter_dict.items():
                if hasattr(table.c, key):
                    column = table.c[key]
                    if isinstance(value, list):
                        stmt = stmt.where(column.in_(value))
                    elif value is None:
                        stmt = stmt.where(column.is_(None))
                    else:
                        stmt = stmt.where(column == value)
                else:
                    return pd.DataFrame()

        # If randomize is True, order the rows randomly.
        if randomize:
            from sqlalchemy import func
            stmt = stmt.order_by(func.random())

        # Apply line limit if specified.
        if line_limit is not None:
            stmt = stmt.limit(line_limit)

        result = self.session.execute(stmt).fetchall()
        df = pd.DataFrame([dict(row._mapping) for row in result])
        return df


    
# To run the test
if __name__ == "__main__":
    db = Database()
    asyncio.run(db.test_database())