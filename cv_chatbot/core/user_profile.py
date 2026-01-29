from typing import List, Optional

# Create a class for the Learning history
class LearningEntry:
    def __init__(
        self,
        program_name: str,
        institution: str,
        status: str,
        focus_areas: Optional[list[str]] = None,
        notes: Optional[str] = None,  
        
    ):

        self.program_name = program_name
        self.institution = institution
        self.status = status # if In progress or Completed
        self.focus_areas = focus_areas
        self.notes = notes

# Store the learning history to a dictionary
    def to_dict(self):
        return {
            "program_name": self.program_name,
            "institution": self.institution,
            "status": self.status,
            "focus_area": self.focus_areas,
            "notes": self.notes,
        }
    
# Create a class for experience history
class ExperienceEntry:
    def __init__(
        self,
        role_title: str,
        organization: str,
        dates: str,
        raw_description: str,
    ):
        
        self.role_title = role_title
        self.organization = organization
        self.dates = dates
        self.raw_description = raw_description

# Store the experience history to a dictionary    
    def to_dict(self):
        return {
            "role_title": self.role_title,
            "organization": self.organization,
            "dates": self.dates,
            "raw_description": self.raw_description,
        }

# Create a class for the user profile
class UserProfile:
    def __init__(
            self,
            full_name: Optional[str] = None,
            email: Optional[str] = None,
            phone: Optional[str] = None,
            target_roles: Optional[list[str]] = None,
    ):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.target_roles = target_roles or []
        
        self.experiences: List[ExperienceEntry] = []
        self.learning_history: list[LearningEntry]= []
        self.declared_skills: List[str] = []
    
    # Add experience history to the profile
    def add_experience(self, experience: ExperienceEntry):
        self.experiences.append(experience)

    # Add learning history to the profile
    def add_learning_entry(self, learning: LearningEntry):
        self.learning_history.append(learning)
    
    # Store the profile a dictionary - One Profile, Multiple CVs for different job spec
    def to_dict(self):
        return {
            "full_name": self.full_name,
            "email": self.email,
            "phone":self.phone,
            "target_roles": self.target_roles,
            "experiences": [e.to_dict() for e in self.experiences],
            "learning_history": [l.to_dict() for l in self.learning_history],
            "declared_skills": self.declared_skills,
        }