from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.sql import Row
from pyspark.sql import HiveContext
from pyspark.sql.functions import *

hive_context = HiveContext(sc)
sqlContext = SQLContext(sc)