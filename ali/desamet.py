# Assume `content_item_id` is the unique identifier for the content item

# Check if the content item exists
if database.exists(content_item_id):
    # If it exists, then delete it
    database.delete(content_item_id)
    print("Content item deleted successfully")
else:
    # If it doesn't exist, no action is necessary
    print("Content item does not exist")
