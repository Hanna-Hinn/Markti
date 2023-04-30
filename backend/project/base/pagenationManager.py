from . import variables


def get_total_pages(sortedList,page_size=10):
    """
    Function :
    Get the total number of pages and total number of records in the data.

    Args:
        page_size (int): Number of records to be displayed per page.

    Returns:
        tuple: (total_pages, total_records) - Total number of pages and total number of records.
    """
    data = sortedList
    if not isinstance(data, list):
        raise ValueError("Data must be a list it is : ", type(data))
    if not isinstance(page_size, int) or page_size < 1:
        raise ValueError("Page size must be a positive integer.")

    total_records = len(data)
    total_pages = (total_records + page_size - 1) // page_size  # integer division with ceiling

    return total_pages, total_records


def paginate(sortedList,page_number=1, page_size=10):
 

    """
    Function :
    Retrieve a page of data based on the given page number and page size.

    Args:
        page_number (int, optional): Page number to retrieve (default is 1).
        page_size (int, optional): Number of records to be displayed per page (default is 10).

    Returns:
        list: Data records for the requested page.
    """
    total_pages, total_records = get_total_pages(sortedList,page_size)
    data = sortedList
    
    if page_number > total_pages:
        raise ValueError("Page number exceeds total number of pages.")

    start = (page_number - 1) * page_size
    end = min(start + page_size, total_records)

    return data[start:end]


