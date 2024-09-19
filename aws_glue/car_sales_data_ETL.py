import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1726758356468 = glueContext.create_dynamic_frame.from_catalog(database="project_db", table_name="csv_files", transformation_ctx="AWSGlueDataCatalog_node1726758356468")

# Script generated for node Change Schema
ChangeSchema_node1726758406985 = ApplyMapping.apply(frame=AWSGlueDataCatalog_node1726758356468, mappings=[("id", "long", "id", "long"), ("age", "long", "age", "long"), ("gender", "long", "gender", "long"), ("race", "long", "race", "long"), ("driving_experience", "long", "driving_experience", "long"), ("education", "long", "education", "long"), ("income", "long", "income", "long"), ("credit_score", "double", "credit_score", "double"), ("vehicle_ownership", "long", "vehicle_ownership", "long"), ("vehicle_year", "long", "vehicle_year", "long"), ("married", "long", "married", "long"), ("children", "long", "children", "long"), ("postal_code", "long", "postal_code", "long"), ("annual_mileage", "double", "annual_mileage", "double"), ("vehicle_type", "long", "vehicle_type", "long"), ("speeding_violations", "long", "speeding_violations", "long"), ("duis", "long", "duis", "long"), ("past_accidents", "long", "past_accidents", "long"), ("outcome", "long", "outcome", "long")], transformation_ctx="ChangeSchema_node1726758406985")

# Script generated for node Amazon S3
AmazonS3_node1726758441164 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1726758406985, connection_type="s3", format="glueparquet", connection_options={"path": "s3://car-sales-dt/target-data-folder/parquet-files/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1726758441164")

job.commit()