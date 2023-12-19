import uuid

from django.db import models
from patient.models import Patient
from account.models import User


class TasksAbstract(models.Model):
    DOCUMENTATION_ROLES = (
        ("Parkinson Nurse", "Parkinson Nurse"),
        ("TeleNurse", "TeleNurse"),
        ("Pflegedienst", "Pflegedienst"),
        ("Neurologen", "Neurologen"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, related_name='%(class)s_creator', on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, related_name='%(class)s_patient', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(max_length=50, null=True, blank=True)
    documentation_role = models.CharField(max_length=50, choices=DOCUMENTATION_ROLES, blank=True, null=True)
    code = models.CharField(max_length=10, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class InitialExamination(TasksAbstract):
    centrePick = models.CharField(max_length=255, blank=True)


class InstructionWearable(TasksAbstract):
    centrePick = models.CharField(max_length=255, blank=True)


class InitialInterviewTelephone(TasksAbstract):
    conversation_reason = models.CharField(max_length=255, blank=True)


class DataReviewProcessing(TasksAbstract):
    duration_month = models.TimeField(null=True, blank=True)


class TelephoneConsultation(TasksAbstract):
    REASONS = (
        (1, "Besprechung einer Verschlechterung/ Veränderung"),
        (2, "Kontaktwunsch der/ des Patient*in"),
        (3, "Unregelmäßige Nutzung des Monitorings"),
        (4, "Nachbesprechung Pflegekonsil"),
        (5, "Nachbesprechung zu Empfehlung/en (nach 14 Tagen)"),
        (6, "Folgetelefonat nach Krankenhausaufenthalt "),
        (7, "Follow-up - 2 Monate keine Verschlechterung"),
        (8, "Freitext - Sonstige Inhalte, und zwar: "),
    )
    consultation_reason = models.CharField(max_length=5, choices=REASONS, blank=True)
    consultation_by = models.ManyToManyField(User, blank=True)
    conversation_topics = models.TextField(blank=True)
    recommendations = models.TextField(blank=True)
    recommendation_issued = models.TextField(blank=True)
    others = models.TextField(blank=True)


class FeedbackCareTeamTelephoneConsultation(models.Model):
    feedback_receiver = (
        ("Parkinson Nurse", "Parkinson Nurse"),
        ("TeleNurse", "TeleNurse"),
        ("Pflegedienst", "Pflegedienst"),
        ("Facharzt", "Facharzt"),
        ("extern", "extern"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, related_name='%(class)s_creator', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, related_name='%(class)s_patient', on_delete=models.CASCADE)
    code = models.CharField(max_length=10, null=True, blank=True)
    feedback_necessary = models.BooleanField(default=False)
    feedback_questions = models.TextField(blank=True)
    feedback_to = models.CharField(max_length=225, blank=True, choices=feedback_receiver)
    recommendations = models.TextField(blank=True)
    visit_reason = models.TextField(blank=True)


class CaseReviewNurseCouncil(TasksAbstract):
    second_visit_required = models.BooleanField(default=False)
    participants = models.ManyToManyField(User, max_length=255, blank=True)
    discussed_issues = models.TextField(blank=True)
    specialist_consultation_required = models.BooleanField(default=False)
    recommendations = models.TextField(blank=True)
    recommendation_issued = models.TextField(blank=True)
    anamnese_discussed = models.TextField(blank=True)


class CaseReviewCouncil(TasksAbstract):
    participants = models.ManyToManyField(User, max_length=255, blank=True)
    anamnese_discussed = models.TextField(blank=True)


class CaseReview(TasksAbstract):
    participants = models.ManyToManyField(User, max_length=255, blank=True)
    anamnese_discussed = models.TextField(blank=True)


class Consultation(TasksAbstract):
    doctor_initials = models.CharField(max_length=255, blank=True)
    decisions = models.TextField(blank=True)
    reason_for_admission = models.TextField(blank=True)
    hospital_admission_required = models.BooleanField(default=False)
    clinic_appointment_required = models.BooleanField(default=False)
    reason_for_clinic_appointment = models.TextField(blank=True)
    measures_after_appointment = models.TextField(blank=True)
    measures_taken = models.TextField(blank=True)


class Visit(TasksAbstract):
    participants = models.ManyToManyField(User, max_length=255, blank=True)
    visit_reason = models.TextField(blank=True)
    misc_documentation = models.TextField(blank=True)


class Equipment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    equipment = models.CharField(max_length=225, blank=True)
    created_at = models.CharField(max_length=10, blank=True)
    removed_at = models.CharField(max_length=10, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    note = models.TextField()


class Individual(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.CharField(max_length=10, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, related_name='individual', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
