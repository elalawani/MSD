from django.db import transaction
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from . import models
from patient.models import Patient


@api_view(['GET'])
def initial_examination_list(request, patient_id):
    if not Patient.objects.filter(id=patient_id).exists():
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
    initial_examination = models.InitialExamination.objects.filter(patient_id=patient_id)
    serializer = InitialExaminationSerializer(initial_examination, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def initial_examination_create(request):
    data = request.data.copy()
    serializer = InitialExaminationSerializer(data=data)
    if serializer.is_valid():
        try:
            with transaction.atomic():
                initial_examination = serializer.save(created_by=request.user)
                initial_examination.refresh_from_db()
                serializer = InitialExaminationSerializer(initial_examination)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def instruction_wearables_list(request, patient_id):
    if not Patient.objects.filter(id=patient_id).exists():
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
    instruction_wearables = models.InstructionWearable.objects.filter(patient_id=patient_id)
    serializer = InstructionWearableSerializer(instruction_wearables, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def instruction_wearables_create(request):
    data = request.data.copy()
    serializer = InstructionWearableSerializer(data=data)
    if serializer.is_valid():
        try:
            with transaction.atomic():
                instruction_wearables = serializer.save(created_by=request.user)
                instruction_wearables.refresh_from_db()
                serializer = InstructionWearableSerializer(instruction_wearables)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def initial_interview_telephones_list(request, patient_id):
    if not Patient.objects.filter(id=patient_id).exists():
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
    initial_interview_telephones = models.InitialInterviewTelephone.objects.filter(patient_id=patient_id)
    serializer = InitialInterviewTelephoneSerializer(initial_interview_telephones, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def initial_interview_telephones_create(request):
    data = request.data.copy()
    serializer = InitialInterviewTelephoneSerializer(data=data)
    if serializer.is_valid():
        try:
            with transaction.atomic():
                interview_telephones = serializer.save(created_by=request.user)
                interview_telephones.refresh_from_db()
                serializer = InitialInterviewTelephoneSerializer(interview_telephones)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def data_review_processing_list(request, patient_id):
    if not Patient.objects.filter(id=patient_id).exists():
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
    data_review_processing = models.DataReviewProcessing.objects.filter(patient_id=patient_id)
    serializer = DataReviewProcessingSerializer(data_review_processing, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def data_review_processing_create(request):
    data = request.data.copy()
    serializer = DataReviewProcessingSerializer(data=data)
    if serializer.is_valid():
        try:
            with transaction.atomic():
                processing = serializer.save(created_by=request.user)
                processing.refresh_from_db()
                serializer = DataReviewProcessingSerializer(processing)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def telephone_consultations_list(request, patient_id):
    if not Patient.objects.filter(id=patient_id).exists():
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
    telephone_consultations = models.TelephoneConsultation.objects.filter(patient_id=patient_id)
    serializer = TelephoneConsultationSerializer(telephone_consultations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def telephone_consultations_create(request):
    data = request.data.copy()
    consultation_by = data.pop('consultation_by')
    serializer = TelephoneConsultationSerializer(data=data)
    if serializer.is_valid():
        consultation = serializer.save(created_by=request.user)
        consultation.consultation_by.set(consultation_by)
        consultation.refresh_from_db()
        serializer = TelephoneConsultationSerializer(consultation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def consultation_reason_choices(request):
    choices = dict(TelephoneConsultation.REASONS)
    choices_list = [{'id': k, 'text': v} for k, v in choices.items()]
    return Response(choices_list)


@api_view(['GET'])
def feedback_care_team_telephone_consultation_choices(request):
    choices = dict(FeedbackCareTeamTelephoneConsultation.feedback_receiver)
    choices_list = [{'id': k, 'text': v} for k, v in choices.items()]
    return Response(choices_list)


@api_view(['GET'])
def feedback_care_team_telephone_consultation_list(request, patient_id):
    if not Patient.objects.filter(id=patient_id).exists():
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
    feedback_care_team_telephone_consultation = \
        models.FeedbackCareTeamTelephoneConsultation.objects.filter(patient_id=patient_id)
    serializer = FeedbackCareTeamTelephoneConsultationSerializer(feedback_care_team_telephone_consultation, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def feedback_care_team_telephone_consultation_create(request):
    serializer = FeedbackCareTeamTelephoneConsultationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def case_review_nurse_council_list(request, patient_id):
    if not Patient.objects.filter(id=patient_id).exists():
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
    case_review_nurse_council = models.CaseReviewNurseCouncil.objects.filter(patient_id=patient_id)
    serializer = CaseReviewNurseCouncilSerializer(case_review_nurse_council, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def case_review_nurse_council_create(request):
    data = request.data.copy()
    participants = data.pop('participants')
    serializer = CaseReviewNurseCouncilSerializer(data=data)
    if serializer.is_valid():
        case_review = serializer.save(created_by=request.user)
        case_review.participants.set(participants)
        case_review.refresh_from_db()
        serializer = CaseReviewNurseCouncilSerializer(case_review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def case_review_council_list(request, patient_id):
    if not Patient.objects.filter(id=patient_id).exists():
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
    case_review_council = models.CaseReviewCouncil.objects.filter(patient_id=patient_id)
    serializer = CaseReviewCouncilSerializer(case_review_council, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def case_review_council_create(request):
    data = request.data.copy()
    participants = data.pop('participants')
    serializer = CaseReviewCouncilSerializer(data=data)
    if serializer.is_valid():
        case_review = serializer.save(created_by=request.user)
        case_review.participants.set(participants)
        case_review.refresh_from_db()
        serializer = CaseReviewCouncilSerializer(case_review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def case_review_create(request):
    data = request.data.copy()
    participants = data.pop('participants')
    serializer = CaseReviewSerializer(data=data)
    if serializer.is_valid():
        case_review = serializer.save(created_by=request.user)
        case_review.participants.set(participants)
        case_review.refresh_from_db()
        serializer = CaseReviewSerializer(case_review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def case_review_list(request, patient_id):
    case_reviews = models.CaseReview.objects.filter(patient_id=patient_id)
    serializer = CaseReviewSerializer(case_reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def consultation_list(request, patient_id):
    if not Patient.objects.filter(id=patient_id).exists():
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
    consultation = models.Consultation.objects.filter(patient_id=patient_id)
    serializer = ConsultationSerializer(consultation, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def consultation_create(request):
    serializer = ConsultationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def visit_list(request, patient_id):
    if not Patient.objects.filter(id=patient_id).exists():
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
    visit = models.Visit.objects.filter(patient_id=patient_id)
    serializer = VisitSerializer(visit, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def visit_create(request):
    data = request.data.copy()
    participants = data.pop('participants')
    serializer = VisitSerializer(data=data)
    if serializer.is_valid():
        visit = serializer.save(created_by=request.user)
        visit.participants.set(participants)
        visit.refresh_from_db()
        serializer = VisitSerializer(visit)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def equipment_list(request, patient_id):
    if not Patient.objects.filter(id=patient_id).exists():
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
    equipment = models.Equipment.objects.filter(patient_id=patient_id)
    serializer = EquipmentSerializer(equipment, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def equipment_create(request):
    serializer = EquipmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['post'])
def create_docu_individual(request):
    data = request.data.copy()
    serializer = IndividualSerializer(data=data)
    if serializer.is_valid():
        try:
            with transaction.atomic():
                processing = serializer.save(user=request.user)
                processing.refresh_from_db()
                serializer = IndividualSerializer(processing)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_individual_docu(request, patient_id):
    if not Patient.objects.filter(id=patient_id).exists():
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
    individual = models.Individual.objects.filter(patient=patient_id)
    serializer = IndividualSerializer(individual, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

