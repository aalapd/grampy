class LoginError(Exception):
    """Raised when login fails after maximum attempts"""
    pass

class UploadError(Exception):
    """Raised when image upload fails after maximum attempts"""
    pass

class NoImagesError(Exception):
    """Raised when there are no images to post"""
    pass