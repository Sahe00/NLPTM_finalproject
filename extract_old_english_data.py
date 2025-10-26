import xml.etree.ElementTree as ET

dataset_root = "./dataset"
parsed_dataset_root = "./parsed_dataset"
old_english_files = ["oracc_cams.vrt", "oracc_dcclt.vrt", "oracc_ribo.vrt", "oracc_rinap.vrt", "oracc_saao.vrt"]

# Store all translations
all_translations = []

def extract_translations_from_file(file_path):
    """Extract translations from a file with multiple XML text elements"""
    translations = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content by </text> and process each text element
    text_elements = content.split('</text>')
    
    for i, text_chunk in enumerate(text_elements[:-1]):  # Skip the last empty chunk
        # Add back the closing tag and wrap in a root element
        xml_content = f"<root>{text_chunk}</text></root>"
        
        try:
            root = ET.fromstring(xml_content)
            sentences = root.findall(".//sentence")
            
            for sentence in sentences:
                translation = sentence.get("translation")
                if translation:
                    # Clean up HTML entities and quotes
                    translation = translation.replace('&quot;', '"')
                    translations.append(translation)
                    
        except ET.ParseError as e:
            print(f"    Warning: Error parsing text element {i+1}: {e}")
            continue
    
    return translations

for file in old_english_files:
    file_path = f"{dataset_root}/{file}"
    print(f"Processing {file}...")
    
    try:
        translations = extract_translations_from_file(file_path)
        
        print(f"  Found {len(translations)} translations")
        all_translations.extend(translations)
        
        output_file = parsed_dataset_root + f"/translations_{file.replace('.vrt', '.txt')}"
        with open(output_file, 'w', encoding='utf-8') as f:
            for translation in translations:
                f.write(translation + '\n')
        print(f"  Saved to {output_file}")
        
    except FileNotFoundError:
        print(f"  File not found: {file_path}")
    except Exception as e:
        print(f"  Error processing {file}: {e}")
