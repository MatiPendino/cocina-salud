
def get_len_number_stars(ratings, filter_rating):
    return len([rating for rating in ratings if rating == filter_rating])