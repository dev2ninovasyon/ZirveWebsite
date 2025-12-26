from PIL import Image

# Paths
source_path = r"C:/Users/lenov/.gemini/antigravity/brain/8ba51c1e-7863-4401-a28b-ae86d1971906/banner_clean_1766650495092.png"
output_path = r"c:\Users\lenov\ZirveWebsite\assets\images\banner\banner.jpg"

try:
    img = Image.open(source_path)
    # The image is likely square-ish.
    
    # We want 1920x650.
    target_width = 1920
    target_height = 650
    
    aspect_ratio = img.height / img.width
    new_height = int(target_width * aspect_ratio)
    img_resized = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
    
    # Crop to 1920x650.
    # Same logic as before: Center crop (vertical).
    if new_height > target_height:
        top = (new_height - target_height) // 2
        bottom = top + target_height
        img_cropped = img_resized.crop((0, top, target_width, bottom))
    else:
        img_cropped = img_resized

    img_cropped.save(output_path, quality=95)
    print("Processed and saved clean banner.jpg")

except Exception as e:
    print(e)
