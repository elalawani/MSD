from rest_framework import serializers
from .models import *
from account.serializers import UserSerializer
from patient.serializers import PatientSerializer


class TasksAbstractSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = TasksAbstract
        fields = ('duration', 'documentation_role', 'code', 'created_by', 'patient', 'created_at', 'note')


class InitialExaminationSerializer(TasksAbstractSerializer):
    class Meta(TasksAbstractSerializer.Meta):
        model = InitialExamination
        fields = TasksAbstractSerializer.Meta.fields + ('centrePick',)


class InstructionWearableSerializer(TasksAbstractSerializer):
    class Meta(TasksAbstractSerializer.Meta):
        model = InstructionWearable
        fields = TasksAbstractSerializer.Meta.fields + ('centrePick',)


class InitialInterviewTelephoneSerializer(TasksAbstractSerializer):
    class Meta(TasksAbstractSerializer.Meta):
        model = InitialInterviewTelephone
        fields = TasksAbstractSerializer.Meta.fields + ('conversation_reason',)


class DataReviewProcessingSerializer(TasksAbstractSerializer):
    class Meta(TasksAbstractSerializer.Meta):
        model = DataReviewProcessing
        fields = TasksAbstractSerializer.Meta.fields + ('duration_month',)


class TelephoneConsultationSerializer(TasksAbstractSerializer):
    consultation_by = UserSerializer(many=True, read_only=True)

    class Meta(TasksAbstractSerializer.Meta):
        model = TelephoneConsultation
        fields = TasksAbstractSerializer.Meta.fields + ('consultation_reason', 'consultation_by', 'conversation_topics',
                                                        'recommendations', 'recommendation_issued', 'others',)


class FeedbackCareTeamTelephoneConsultationSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = FeedbackCareTeamTelephoneConsultation
        fields = "__all__"


class CaseReviewNurseCouncilSerializer(TasksAbstractSerializer):
    participants = UserSerializer(many=True, read_only=True)

    class Meta(TasksAbstractSerializer.Meta):
        model = CaseReviewNurseCouncil
        fields = TasksAbstractSerializer.Meta.fields + ('second_visit_required', 'participants', 'discussed_issues',
                                                        'specialist_consultation_required', 'recommendations',
                                                        'recommendation_issued', 'anamnese_discussed',)


class CaseReviewCouncilSerializer(TasksAbstractSerializer):
    participants = UserSerializer(many=True, read_only=True)

    class Meta(TasksAbstractSerializer.Meta):
        model = CaseReviewCouncil
        fields = TasksAbstractSerializer.Meta.fields + ('participants', 'anamnese_discussed',)


class CaseReviewSerializer(TasksAbstractSerializer):
    participants = UserSerializer(many=True, read_only=True)

    class Meta(TasksAbstractSerializer.Meta):
        model = CaseReview
        fields = TasksAbstractSerializer.Meta.fields + ('participants', 'anamnese_discussed',)


class ConsultationSerializer(TasksAbstractSerializer):
    class Meta(TasksAbstractSerializer.Meta):
        model = Consultation
        fields = TasksAbstractSerializer.Meta.fields + (
            'doctor_initials',
            'decisions',
            'reason_for_admission',
            'hospital_admission_required',
            'clinic_appointment_required',
            'reason_for_clinic_appointment',
            'measures_after_appointment',
            'measures_taken'
        )


class VisitSerializer(TasksAbstractSerializer):
    participants = UserSerializer(many=True, read_only=True)

    class Meta(TasksAbstractSerializer.Meta):
        model = Visit
        fields = TasksAbstractSerializer.Meta.fields + ('participants',)


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"


class IndividualSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Individual
        fields = "__all__"
