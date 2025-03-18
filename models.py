import shortuuid
from database import urls_collection

def shorten_url(original_url):
    """Generates a short ID and saves the URL mapping in MongoDB."""
    short_id = shortuuid.uuid()[:6]  # Generate a 6-character short ID
    urls_collection.insert_one({"short_id": short_id, "original_url": original_url})
    return short_id

def get_original_url(short_id):
    """Retrieves the original URL from MongoDB."""
    result = urls_collection.find_one({"short_id": short_id})
    return result["original_url"] if result else None
