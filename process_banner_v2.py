from PIL import Image

# Paths
source_path = r"C:/Users/lenov/.gemini/antigravity/brain/8ba51c1e-7863-4401-a28b-ae86d1971906/banner_restored_1766650203481.png"
output_path = r"c:\Users\lenov\ZirveWebsite\assets\images\banner\banner.jpg"

try:
    img = Image.open(source_path)
    # The image is likely 1024x1024 because the model outputs square by default if not strictly controlled or if input was square-ish (input was 1024x432 though).
    # Step 42 result looks square in the preview.
    
    # We want 1920x650.
    # If we just resize 1024x1024 -> 1920x1920, and crop 650 height, we might lose top/bottom.
    # The content (text + boat + logos) is everything.
    # The text is at top, logos at bottom.
    
    # Let's resize width to 1920.
    target_width = 1920
    aspect_ratio = img.height / img.width
    new_height = int(target_width * aspect_ratio)
    img_resized = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
    
    # Now we need to crop to height 650.
    # If new_height > 650, crop from center?
    # But wait, looking at the square result, it seems to have added empty space or stretched?
    # Actually, the result shows the full content in a square.
    # So shrinking height to 650 (approx 1/3 of width) implies we must CROP significantly or SQUASH.
    # We cannot squash.
    # The original was panoramic. The AI result is square.
    # This means the AI added blue sky on top and water on bottom?
    # Or it squashed the content?
    # Looking at the preview, the boat and text look normal aspect ratio.
    # So there must be a lot of extra space.
    
    # Let's try to fit 1920x650.
    # We want to keep the center part where text and boat are.
    # 650 is about 34% of 1920.
    # The image has text at top, boat in middle, logos at bottom.
    # If we crop, we lose something.
    # UNLESS the AI result has a lot of padding.
    
    # Let's crop centered vertically.
    target_height = 650
    if new_height > target_height:
        top = (new_height - target_height) // 2
        bottom = top + target_height
        
        # Check if logos are cut.
        # Logos are at the very bottom.
        # We might need to crop from the bottom up? Or crop the top?
        # Let's crop to keep the content centered visually.
        # Best bet: Resize such that the content fits in 650 height? No, that would make width tiny.
        
        # Strategy:
        # Resize text/boat section separately? No.
        
        # Let's assume the "meaningful" content is in the middle-ish.
        # We will try to crop from center.
        # BUT, looking at the square square, there is a lot of blue sky.
        # Maybe we crop the top mostly?
        
        # Let's try to find the content bounds? Too complex.
        
        # Alternative: The user wants "aynı boyutta" as the original.
        # The user's original was 1024x432 (approx 2.37 ratio).
        # 1024x432 is very close to 1920x810.
        # 1920x650 is 2.95 ratio (more panoramic).
        
        # Let's crop the image to 1920x650 by removing top sky.
        # Text is below the top edge.
        
        # Calculation:
        # Resize to Width 1920.
        # Calculate new height.
        # Crop (new_height - 650) from the TOP mainly, but keep some space above text.
        # Actually, let's crop from center but shift up/down if needed.
        
        # Let's assume center crop is safe for now, but bias it downwards (keep bottom logos).
        # Logos are critical.
        # New bottom = new_height.
        # New top = new_height - 650.
        # Does this cut text?
        
        # Let's force the resize to be unproportional? No, looks bad.
        
        # Let's try to crop center.
        img_cropped = img_resized.crop((0, (new_height - 650) // 2, target_width, (new_height + 650) // 2))
    else:
        # Image is shorter than 650? Unlikely if it's square.
        img_cropped = img_resized

    img_cropped.save(output_path, quality=95)
    print("Processed and saved banner.jpg")

except Exception as e:
    print(e)
