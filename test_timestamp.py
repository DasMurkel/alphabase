#!/usr/bin/env python3

from datetime import date, datetime, timedelta
import timestamp as ts
import alphabase as ab


def test_time_to_version():
    assert ts.time_to_version(ts.START) == "000"


BASE = ab.alphabase(ts.WINDOWS_1252_ALPHABET)
MAX_VAL = BASE.max_value(ts.MAX_CHARACTERS)


def test_time_to_version_rollover():
    
    td = timedelta(minutes=MAX_VAL)
    assert ts.time_to_version(ts.START + td) == "000"


def test_version_to_time():
    ts.START = datetime.now()
    assert ts.version_to_time("000") == ts.START
    assert ts.version_to_time("001") == ts.START + timedelta(minutes=1)


def test_version_to_time_rollback():
    now = datetime.now() # Have to store temporary, otherwise, there is a difference in nanoseconds :D
    # Move ts.START back to provoke a rollover
    ts.START = now - timedelta(minutes=MAX_VAL)
    assert ts.version_to_time("000") == now

