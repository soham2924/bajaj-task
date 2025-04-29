import re

def extract_lab_tests(text: str):
    pattern = r"(?P<test_name>[A-Za-z \(\)\-/]+?)\s+(?P<value>\d+\.?\d*)\s*(?P<units>[a-zA-Z/%]+)?\s+(?P<range>\d+\.?\d*\s*-\s*\d+\.?\d*)"
    matches = re.finditer(pattern, text)

    results = []
    for match in matches:
        test_name = match.group("test_name").strip()
        value = float(match.group("value"))
        ref_range = match.group("range").replace(" ", "")
        ref_low, ref_high = map(float, ref_range.split('-'))

        results.append({
            "lab_test_name": test_name,
            "lab_test_value": value,
            "bio_reference_range": f"{ref_low}-{ref_high}",
            "lab_test_out_of_range": value < ref_low or value > ref_high
        })

    return results
