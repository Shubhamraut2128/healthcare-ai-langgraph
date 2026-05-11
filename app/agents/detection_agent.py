def detection_agent(state):

    text = state["extracted_text"].lower()

    disease = "Unknown"

    if "pneumonia" in text:
        disease = "Pneumonia"

    elif "cancer" in text:
        disease = "Cancer"

    elif "diabetes" in text:
        disease = "Diabetes"

    return {
        "disease": disease
    }