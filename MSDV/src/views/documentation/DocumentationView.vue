<template>
    <div class="container">
        <div class="border-b border-b-slate-500">
            <div
                class="p-2 hover:cursor-pointer bg-sky-700 m-2 rounded-full flex w-fit"
            >
                <button v-if="documentations" @click="toggleDocumentationPage">
                    zurück zur Documentation
                </button>
                <button v-else @click="toggleDocumentationPage">
                    individulle Documentation
                </button>
            </div>
        </div>
        <div v-if="documentations">
            <individual-docu />
        </div>
        <div v-else class="container flex flex-row">
            <div class="flex flex-col grow w-full">
                <div v-if="dataView === 'examination' || dataView === ''">
                    <initial-examinations />
                </div>
                <div v-if="dataView === 'wearables'">
                    <instruction-wearables />
                </div>
                <div v-if="dataView === 'interview-telephones'">
                    <initial-interview-telephones />
                </div>
                <div v-if="dataView === 'feedback'">
                    <feedback-care-team-telephone-consultation />
                </div>
                <div v-if="dataView === 'equipment'">
                    <equipment />
                </div>
                <div v-if="dataView === 'visit'">
                    <visit />
                </div>
                <div v-if="dataView === 'processing'">
                    <data-review-processing />
                </div>
                <div v-if="dataView === 'case-review'">
                    <case-review />
                </div>
                <div v-if="dataView === 'case-review-council'">
                    <case-review-council />
                </div>
                <div v-if="dataView === 'case-review-nurse-council'">
                    <case-review-nurse-council />
                </div>
                <div v-if="dataView === 'telephone-consultation'">
                    <telephone-consultations />
                </div>
                <div v-if="dataView === 'consultation'">
                    <consultation />
                </div>
            </div>
            <div class="right flex flex-col w-1/2 p-2">
                <div class="mb-16 space-y-2 flex flex-col items-center">
                    <router-link
                        :to="`/details/${id}/create_documentation`"
                        class="p-2 bg-sky-700 rounded"
                    >
                        add +
                    </router-link>
                </div>
                <div class="flex flex-col w-full h-96 overflow-auto">
                    <button
                        :class="
                            dataView === 'examination' || dataView === ''
                                ? ' font-extrabold text-lg'
                                : ''
                        "
                        class="px-3 py-2 rounded dark:bg-slate-600 bg-sky-700 m-1"
                        @click="dataView = 'examination'"
                    >
                        Initial Examinations
                    </button>
                    <button
                        :class="
                            dataView === 'wearables'
                                ? ' font-extrabold text-lg'
                                : ''
                        "
                        class="px-3 py-2 rounded dark:bg-slate-600 bg-sky-700 m-1"
                        @click="dataView = 'wearables'"
                    >
                        Instruction wearables
                    </button>
                    <button
                        :class="
                            dataView === 'interview-telephones'
                                ? ' font-extrabold text-lg'
                                : ''
                        "
                        class="px-3 py-2 rounded dark:bg-slate-600 bg-sky-700 m-1"
                        @click="dataView = 'interview-telephones'"
                    >
                        interview telephones
                    </button>
                    <button
                        :class="
                            dataView === 'feedback'
                                ? ' font-extrabold text-lg'
                                : ''
                        "
                        class="px-3 py-2 rounded dark:bg-slate-600 bg-sky-700 m-1"
                        @click="dataView = 'feedback'"
                    >
                        feedback consultation
                    </button>
                    <button
                        :class="
                            dataView === 'equipment'
                                ? ' font-extrabold text-lg'
                                : ''
                        "
                        class="px-3 py-2 rounded dark:bg-slate-600 bg-sky-700 m-1"
                        @click="dataView = 'equipment'"
                    >
                        equipment
                    </button>
                    <button
                        :class="
                            dataView === 'visit'
                                ? ' font-extrabold text-lg'
                                : ''
                        "
                        class="px-3 py-2 rounded dark:bg-slate-600 bg-sky-700 m-1"
                        @click="dataView = 'visit'"
                    >
                        visit
                    </button>
                    <button
                        :class="
                            dataView === 'processing'
                                ? ' font-extrabold text-lg'
                                : ''
                        "
                        class="px-3 py-2 rounded dark:bg-slate-600 bg-sky-700 m-1"
                        @click="dataView = 'processing'"
                    >
                        processing
                    </button>
                    <button
                        :class="
                            dataView === 'case-review'
                                ? ' font-extrabold text-lg'
                                : ''
                        "
                        class="px-3 py-2 rounded dark:bg-slate-600 bg-sky-700 m-1"
                        @click="dataView = 'case-review'"
                    >
                        case review
                    </button>
                    <button
                        :class="
                            dataView === 'case-review-council'
                                ? ' font-extrabold text-lg'
                                : ''
                        "
                        class="px-3 py-2 rounded dark:bg-slate-600 bg-sky-700 m-1"
                        @click="dataView = 'case-review-council'"
                    >
                        case review council
                    </button>
                    <button
                        :class="
                            dataView === 'case-review-nurse-council'
                                ? ' font-extrabold text-lg'
                                : ''
                        "
                        class="px-3 py-2 rounded dark:bg-slate-600 bg-sky-700 m-1"
                        @click="dataView = 'case-review-nurse-council'"
                    >
                        case review nurse-council
                    </button>
                    <button
                        :class="
                            dataView === 'telephone-consultation'
                                ? ' font-extrabold text-lg'
                                : ''
                        "
                        class="px-3 py-2 rounded dark:bg-slate-600 bg-sky-700 m-1"
                        @click="dataView = 'telephone-consultation'"
                    >
                        telephone consultation
                    </button>
                    <button
                        :class="
                            dataView === 'consultation'
                                ? ' font-extrabold text-lg'
                                : ''
                        "
                        class="px-3 py-2 rounded dark:bg-slate-600 bg-sky-700 m-1"
                        @click="dataView = 'consultation'"
                    >
                        consultation
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import InitialExaminations from '@/components/patient/documentation/view/initialExaminations.vue';
import IndividualDocu from '@/components/patient/documentation/view/individualDocu.vue';
import InstructionWearables from '@/components/patient/documentation/view/instructionWearables.vue';
import InitialInterviewTelephones from '@/components/patient/documentation/view/initialInterviewTelephones.vue';
import FeedbackCareTeamTelephoneConsultation from '@/components/patient/documentation/view/feedbackCareTeamTelephoneConsultation.vue';
import Equipment from '@/components/patient/documentation/view/equipment.vue';
import Visit from '@/components/patient/documentation/view/visit.vue';
import DataReviewProcessing from '@/components/patient/documentation/view/dataReviewProcessing.vue';
import CaseReview from '@/components/patient/documentation/view/caseReview.vue';
import CaseReviewCouncil from '@/components/patient/documentation/view/caseReviewCouncil.vue';
import CaseReviewNurseCouncil from '@/components/patient/documentation/view/caseReviewNurseCouncil.vue';
import TelephoneConsultations from '@/components/patient/documentation/view/telephoneConsultations.vue';
import Consultation from '@/components/patient/documentation/view/consultation.vue';
import { useRoute } from 'vue-router';

export default {
    name: 'documentation',
    components: {
        Consultation,
        TelephoneConsultations,
        CaseReviewNurseCouncil,
        CaseReviewCouncil,
        CaseReview,
        DataReviewProcessing,
        Visit,
        Equipment,
        FeedbackCareTeamTelephoneConsultation,
        InitialInterviewTelephones,
        InstructionWearables,
        InitialExaminations,
        IndividualDocu
    },
    data() {
        return {
            dataView: '',
            id: useRoute().params.id,
            documentations: false
        };
    },
    methods: {
        toggleDocumentationPage() {
            this.documentations = !this.documentations;
        }
    }
};
</script>
