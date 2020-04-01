def prediction_class_str(pred):
    map_dict = {
        0: "This person is predicted with a salary that is less than 50K USD per year.",
        1: "This person is predicted with a salary that is more than 50K USD per year."
    }

    return map_dict[pred]