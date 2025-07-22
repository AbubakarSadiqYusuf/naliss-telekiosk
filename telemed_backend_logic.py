# backend_logic.py
from datetime import datetime
import re

# ------------------- PATIENT REGISTRATION -------------------
def generate_patient_id(ghana_card: str, dob: str) -> str:
    """
    Generate a unique Patient ID based on Ghana Card and DOB.
    Format: P-[Last4DigitsOfGhanaCard]-[YYMMDD]
    """
    last4 = re.sub(r'\D', '', ghana_card)[-4:]
    dob_obj = datetime.strptime(dob, "%Y-%m-%d")
    return f"P-{last4}-{dob_obj.strftime('%y%m%d')}"

# ------------------- CLINICIAN REGISTRATION -------------------
def get_role_code(field: str) -> str:
    role_map = {
        'General Practitioner': 'GPR',
        'Surgeon': 'SUR',
        'Nurse': 'NUR',
        'Telemedicine': 'TEL',
        'Cardiologist': 'CAR',
        'Pediatrician': 'PED'
    }
    return role_map.get(field, 'UNK')

def generate_clinician_id(name: str, staff_id: str, field: str) -> str:
    """
    Format: [RoleCode]-[Initials]-[Last4OfStaffID]
    """
    initials = ''.join([n[0] for n in name.strip().split() if n])
    last4 = re.sub(r'\D', '', staff_id)[-4:]
    return f"{get_role_code(field)}-{initials.upper()}-{last4}"

# ------------------- REFERRAL LOGIC -------------------
def assign_clinician_by_condition(condition: str) -> str:
    """
    Assigns clinician field based on referral condition.
    """
    condition = condition.lower()
    if "cardiac" in condition:
        return "CAR"
    elif "child" in condition or "pediatric" in condition:
        return "PED"
    elif "surgery" in condition or "post-op" in condition:
        return "SUR"
    elif "monitoring" in condition or "remote" in condition:
        return "TEL"
    elif "fever" in condition or "checkup" in condition:
        return "GPR"
    else:
        return "GPR"  # default fallback

# ------------------- SAMPLE USAGE -------------------
if __name__ == "__main__":
    # Patient Example
    patient_id = generate_patient_id("GHA-3245678236723", "2001-02-01")
    print(f"Generated Patient ID: {patient_id}")

    # Clinician Example
    clinician_id = generate_clinician_id("John Kwame Mensah", "UGHS-00452", "General Practitioner")
    print(f"Generated Clinician ID: {clinician_id}")

    # Referral Assignment
    condition = "Post-surgery fever with monitoring needed"
    assigned_field = assign_clinician_by_condition(condition)
    print(f"Assigned Clinician Field: {assigned_field}")
