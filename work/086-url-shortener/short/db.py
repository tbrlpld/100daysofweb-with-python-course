

# Get or create table

# >>> table = dynamodb.Table("studd")
# >>> table.table_status
# If table not exists -> botocore.errorfactory.ResourceNotFoundException

# If table exists
# >>> table = dynamodb.Table("urls")
# >>> table.table_status
# 'ACTIVE'
