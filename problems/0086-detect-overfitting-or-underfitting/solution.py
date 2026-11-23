def model_fit_quality(training_accuracy, test_accuracy):
    # Check overfitting first
    if training_accuracy - test_accuracy > 0.2:
        return 1

    # Check underfitting
    elif training_accuracy < 0.7 and test_accuracy < 0.7:
        return -1

    # Otherwise, good fit
    else:
        return 0