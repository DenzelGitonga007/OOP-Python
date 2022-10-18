# Documenting a function
def to_seconds(hours, minutes, seconds):
    #initialize the documentation
    """Converts hours, minutes, and seconds into seconds"""
    return hours*3600 + minutes*60 + seconds
# Ask for help
help(to_seconds)