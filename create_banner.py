from PIL import Image, ImageDraw, ImageFont
import os

# Paths
source_path = r"C:/Users/lenov/.gemini/antigravity/brain/8ba51c1e-7863-4401-a28b-ae86d1971906/banner_centered_1766649938857.png"
output_path = r"c:\Users\lenov\ZirveWebsite\assets\images\banner\banner.jpg"

try:
    img = Image.open(source_path)
    
    # Target dimensions
    target_width = 1920
    target_height = 650
    
    # Resize to width 1920
    aspect_ratio = img.height / img.width
    new_height = int(target_width * aspect_ratio)
    img_resized = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
    
    # Create new canvas
    canvas = Image.new('RGB', (target_width, target_height), (20, 30, 80)) # Dark blue fallback
    
    # Crop the Boat/Middle Section
    # Assuming boat is in the middle. 
    # Let's crop a section of height 650 from the middle.
    mid_y = new_height // 2
    crop_top = mid_y - (target_height // 2)
    crop_bottom = mid_y + (target_height // 2)
    
    # Ensure bounds
    if crop_top < 0: crop_top = 0
    if crop_bottom > new_height: crop_bottom = new_height
    
    boat_strip = img_resized.crop((0, crop_top, target_width, crop_bottom))
    canvas.paste(boat_strip, (0, 0))
    
    # Crop the Logo Section (Bottom)
    # Logos are usually at the very bottom.
    logo_height = 100
    logo_strip = img_resized.crop((0, new_height - logo_height, target_width, new_height))
    
    # Paste logos at bottom of canvas
    canvas.paste(logo_strip, (0, target_height - logo_height))
    
    # Draw Text
    draw = ImageDraw.Draw(canvas)
    
    # Fonts - Try to load system fonts
    try:
        font_title_small = ImageFont.truetype("arial.ttf", 30)
        font_title_large = ImageFont.truetype("arialbd.ttf", 80)
        font_date = ImageFont.truetype("arial.ttf", 60)
    except:
        font_title_small = ImageFont.load_default()
        font_title_large = ImageFont.load_default()
        font_date = ImageFont.load_default()
    
    # Colors
    color_green = (140, 198, 63) # Approx logo green
    color_white = (255, 255, 255)
    
    # Text Content
    text1 = "ESKİŞEHİR MUHASEBE, FİNANS VE VERGİ ZİRVESİ"
    text2 = "ESKISEHIR TALKS"
    text3 = "11-12 Nisan 2026"
    
    # Positioning (Center Top)
    # Helper to center text
    def draw_text_centered(text, font, y, color):
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x = (target_width - text_width) // 2
        
        # Shadow
        draw.text((x+2, y+2), text, font=font, fill=(0,0,0))
        # Text
        draw.text((x, y), text, font=font, fill=color)
        return bbox[3] - bbox[1] # height

    current_y = 50
    h1 = draw_text_centered(text1, font_title_small, current_y, color_green)
    current_y += h1 + 10
    h2 = draw_text_centered(text2, font_title_large, current_y, color_green)
    current_y += h2 + 10
    draw_text_centered(text3, font_date, current_y, color_white)

    # Save
    canvas.save(output_path, quality=95)
    print(f"Successfully created banner at {output_path}")

except Exception as e:
    print(f"Error: {e}")
