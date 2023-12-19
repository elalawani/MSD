<template>
    <div class="p-5 text-slate-900 dark:text-slate-50">
        <router-link
            :to="`/details/${id}/documentation`"
            class="font-extralight hover:text-sky-600"
        >
            &lsaquo; alle dokumentations
        </router-link>
        <div class="flex justify-center p-6 items-center">
            <h1 class="text-4xl">Bitte wählen Sie die Art des Dokuments aus</h1>
        </div>

        <div class="flex overflow-scroll space-x-3">
            <button
                v-for="(myOption, index) in options"
                :key="index"
                :class="
                    option === myOption
                        ? 'border-b border-b-sky-500 text-sky-500 shadow-none'
                        : 'dark:bg-slate-600'
                "
                class="p-4 mb-3 rounded shadow-xl h-20"
                @click="option = myOption"
            >
                {{ myOption }}
            </button>
        </div>
    </div>
    <div v-if="option === 'Fallbesprechung'">
        <create-case-review />
    </div>
    <div v-else-if="option === 'Eingangsuntersuchung'">
        <create-initial-examination />
    </div>
    <div v-else-if="option === 'Wearable'">
        <create-instruction-wearable />
    </div>
    <div v-else-if="option === 'Eingangsgespräch'">
        <create-initial-interview-telephone />
    </div>
    <div v-else-if="option === 'Rückmeldung'">
        <create-feedback-care-team-telephone-consultation />
    </div>
    <div v-else-if="option === 'equipment'">
        <create-equipment />
    </div>
    <div v-else-if="option === 'hausebesuch'">
        <creat-visit />
    </div>
    <div v-else-if="option === 'processing'">
        <create-data-review-processing />
    </div>
    <div v-else-if="option === 'Fallbesprechung-konsil'">
        <creat-case-review-council />
    </div>
    <div v-else-if="option === 'Fallbesprechung-nurse-konsil'">
        <create-case-review-nurse-council />
    </div>
    <div v-else-if="option === 'Konsultation'">
        <create-consultation />
    </div>
    <div v-else-if="option === 'Telefonische-Konsultation'">
        <create-telephone-consultation />
    </div>
    <div v-else>
        <div
            class="text-slate-800 dark:text-slate-100 container flex mt-10 justify-center m-auto text-7xl font-extrabold pb-4"
        >
            noch nichts ausgewählt
        </div>
    </div>
</template>
<script>
import CreateCaseReview from '@/components/patient/documentation/creation/createCaseReview.vue';
import CreateInitialExamination from '@/components/patient/documentation/creation/createInitialExamination.vue';
import CreateInstructionWearable from '@/components/patient/documentation/creation/createInstructionWearable.vue';
import CreateCaseReviewNurseCouncil from '@/components/patient/documentation/creation/createCaseReviewNurseCouncil.vue';
import CreatCaseReviewCouncil from '@/components/patient/documentation/creation/creatCaseReviewCouncil.vue';
import CreateEquipment from '@/components/patient/documentation/creation/createEquipment.vue';
import CreatVisit from '@/components/patient/documentation/creation/creatVisit.vue';
import CreateFeedbackCareTeamTelephoneConsultation from '@/components/patient/documentation/creation/createFeedbackCareTeamTelephoneConsultation.vue';
import CreateDataReviewProcessing from '@/components/patient/documentation/creation/createDataReviewProcessing.vue';
import CreateTelephoneConsultation from '@/components/patient/documentation/creation/createTelephoneConsultation.vue';
import CreateConsultation from '@/components/patient/documentation/creation/createConsultation.vue';
import CreateInitialInterviewTelephone from '@/components/patient/documentation/creation/createInitialInterviewTelephone.vue';
import { useRoute } from 'vue-router';
import InitialInterviewTelephones from '@/components/patient/documentation/view/initialInterviewTelephones.vue';
export default {
    name: 'NewDataFormView',
    data() {
        return {
            option: '',
            id: useRoute().params.id,
            options: [
                'Eingangsuntersuchung',
                'Wearable',
                'Eingangsgespräch',
                'Rückmeldung',
                'equipment',
                'hausebesuch',
                'processing',
                'Fallbesprechung',
                'Fallbesprechung-konsil',
                'Fallbesprechung-nurse-konsil',
                'Konsultation',
                'Telefonische-Konsultation'
            ]
        };
    },

    components: {
        InitialInterviewTelephones,
        CreateCaseReview,
        CreateInitialExamination,
        CreateInstructionWearable,
        CreatVisit,
        CreateEquipment,
        CreateFeedbackCareTeamTelephoneConsultation,
        CreateConsultation,
        CreateCaseReviewNurseCouncil,
        CreateTelephoneConsultation,
        CreateDataReviewProcessing,
        CreatCaseReviewCouncil,
        CreateInitialInterviewTelephone
    }
};
</script>
