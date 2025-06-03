def crop(crop_name):
    crop_data = {
        "coffee": ["/static/images/Coffee.jpg", "Brazil, Vietnam, Colombia, Indonesia", "tropical", "United States, Germany, Italy, Japan"],
        "cotton": ["/static/images/cotton.jpg", "United States, India, Brazil, Pakistan", "tropical", "China, Bangladesh, Egypt"],
        "gram": ["/static/images/gram.jpg", "India, Pakistan, Turkey, Myanmar", "temperate", "Vietnam, Spain, Myanmar"],
        "millets": ["/static/images/Millets.jpeg", "India, Nigeria, Niger, Nepal", "temperate", "United States, United Kingdom, Australia"],
        "oilseeds": ["/static/images/Oilseeds.jpeg", "United States, Brazil, Argentina, China", "tropical", "European Union, China, Japan"],
        "paddy": ["/static/images/Paddy.jpeg", "Thailand, Vietnam, India, Pakistan", "tropical", "Philippines, Nigeria, Saudi Arabia"],
        "sugarcane": ["/static/images/Sugarcane.jpeg", "Brazil, India, Thailand, China", "tropical", "China, Pakistan, Indonesia"],
        "tea": ["/static/images/Tea.jpeg", "China, India, Kenya, Sri Lanka", "temperate", "United Kingdom, Russia, United States, Pakistan"],
        "wheat": ["/static/images/wheat.jpg", "United States, Canada, Russia, France", "temperate", "Indonesia, Egypt, Turkey, Philippines"]
    }
    return crop_data[crop_name]