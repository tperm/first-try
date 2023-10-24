import csv
import psycopg2
import argparse
import sys 
from createtabledupe import createtabledupe


createtabledupe('ph1', '/Users/troyperment/Development/awscloudsync-laptop/', 'brokers', 'troyperment', 'localhost', '5432')