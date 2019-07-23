
def set_images_to_vec(given_images):

    vec_lst = []
    for curr_img in given_images:
        curr_vec = flatten(curr_img)
        vec_lst.append(curr_vec)
    return vec_lst
