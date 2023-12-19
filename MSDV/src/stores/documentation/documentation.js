import { defineStore } from 'pinia';
import axios from 'axios';
import router from '@/router';

export const useDocumentationsStore = defineStore({
    id: 'documentation',

    state: () => ({
        initial_examinations: [],
        instruction_wearables: [],
        initial_interview_telephones: [],
        data_review_processing: [],
        telephone_consultations: [],
        feedback_careTeam_telephone_consultation: [],
        case_review_nurse_council: [],
        case_review_council: [],
        case_review: [],
        consultation: [],
        visit: [],
        equipment: [],
        patientDocu: []
    }),

    actions: {
        get_initial_examinations(patient_id) {
            this.initial_examinations = [];
            return new Promise((resolve, reject) => {
                axios
                    .get(
                        `/api/documentation/initial_examinations/${patient_id}`
                    )
                    .then((response) => {
                        this.initial_examinations = response.data;
                        resolve(this.initial_examinations);
                    })
                    .catch((error) => {
                        console.log('error', error.response.status);
                        reject(error);
                        reject(error);
                        if (error.response && error.response.status === 403) {
                            router.push({ name: 'view' });
                        }
                    });
            });
        },
        get_instruction_wearables(patient_id) {
            this.instruction_wearables = [];
            return new Promise((resolve, reject) => {
                axios
                    .get(
                        `/api/documentation/instruction_wearables/${patient_id}`
                    )
                    .then((response) => {
                        this.instruction_wearables = response.data;
                        resolve(this.instruction_wearables);
                    })
                    .catch((error) => {
                        console.log('error', error.response.status);
                        reject(error);
                        if (error.response && error.response.status === 403) {
                            router.push({ name: 'view' });
                        }
                    });
            });
        },
        get_initial_interview_telephones(patient_id) {
            this.initial_interview_telephones = [];
            return new Promise((resolve, reject) => {
                axios
                    .get(
                        `/api/documentation/initial_interview_telephones/${patient_id}`
                    )
                    .then((response) => {
                        this.initial_interview_telephones = response.data;
                        resolve(this.initial_interview_telephones);
                    })
                    .catch((error) => {
                        console.log('error', error.response.status);
                        reject(error);
                        if (error.response && error.response.status === 403) {
                            router.push({ name: 'view' });
                        }
                    });
            });
        },
        get_data_review_processing(patient_id) {
            this.data_review_processing = [];
            return new Promise((resolve, reject) => {
                axios
                    .get(
                        `/api/documentation/data_review_processing/${patient_id}`
                    )
                    .then((response) => {
                        this.data_review_processing = response.data;
                        resolve(this.data_review_processing);
                    })
                    .catch((error) => {
                        console.log('error', error.response.status);
                        reject(error);
                        if (error.response && error.response.status === 403) {
                            router.push({ name: 'view' });
                        }
                    });
            });
        },
        get_telephone_consultations(patient_id) {
            this.telephone_consultations = [];
            return new Promise((resolve, reject) => {
                axios
                    .get(
                        `/api/documentation/telephone_consultations/${patient_id}`
                    )
                    .then((response) => {
                        this.telephone_consultations = response.data;
                        resolve(this.telephone_consultations);
                    })
                    .catch((error) => {
                        console.log('error', error.response.status);
                        reject(error);
                        if (error.response && error.response.status === 403) {
                            router.push({ name: 'view' });
                        }
                    });
            });
        },
        get_feedback_careTeam_telephone_consultation(patient_id) {
            this.feedback_careTeam_telephone_consultation = [];
            return new Promise((resolve, reject) => {
                axios
                    .get(
                        `/api/documentation/feedback_care_team_telephone_consultation/${patient_id}`
                    )
                    .then((response) => {
                        this.feedback_careTeam_telephone_consultation =
                            response.data;
                        resolve(this.feedback_careTeam_telephone_consultation);
                    })
                    .catch((error) => {
                        console.log('error', error.response.status);
                        reject(error);
                        if (error.response && error.response.status === 403) {
                            router.push({ name: 'view' });
                        }
                    });
            });
        },
        get_case_review_nurse_council(patient_id) {
            this.case_review_nurse_council = [];
            return new Promise((resolve, reject) => {
                axios
                    .get(
                        `/api/documentation/case_review_nurse_council/${patient_id}`
                    )
                    .then((response) => {
                        this.case_review_nurse_council = response.data;
                        resolve(this.case_review_nurse_council);
                    })
                    .catch((error) => {
                        console.log('error', error.response.status);
                        reject(error);
                        if (error.response && error.response.status === 403) {
                            router.push({ name: 'view' });
                        }
                    });
            });
        },
        get_case_review_council(patient_id) {
            this.case_review_council = [];
            return new Promise((resolve, reject) => {
                axios
                    .get(`/api/documentation/case_review_council/${patient_id}`)
                    .then((response) => {
                        this.case_review_council = response.data;
                        resolve(this.case_review_council);
                    })
                    .catch((error) => {
                        console.log('error', error.response.status);
                        reject(error);
                        if (error.response && error.response.status === 403) {
                            router.push({ name: 'view' });
                        }
                    });
            });
        },

        get_equipment(patient_id) {
            this.equipment = [];
            return new Promise((resolve, reject) => {
                axios
                    .get(`/api/documentation/equipment/${patient_id}`)
                    .then((response) => {
                        this.equipment = response.data;
                        resolve(this.equipment);
                    })
                    .catch((error) => {
                        console.log('error', error.response.status);
                        reject(error);
                        reject(error);
                        if (error.response && error.response.status === 403) {
                            router.push({ name: 'view' });
                        }
                    });
            });
        },
        get_visit(patient_id) {
            this.visit = [];
            return new Promise((resolve, reject) => {
                axios
                    .get(`/api/documentation/visit/${patient_id}`)
                    .then((response) => {
                        this.visit = response.data;
                        resolve(this.visit);
                    })
                    .catch((error) => {
                        console.log('error', error.response.status);
                        reject(error);
                        if (error.response && error.response.status === 403) {
                            router.push({ name: 'view' });
                        }
                    });
            });
        },
        get_consultation(patient_id) {
            this.consultation = [];
            return new Promise((resolve, reject) => {
                axios
                    .get(`/api/documentation/consultation/${patient_id}`)
                    .then((response) => {
                        this.consultation = response.data;
                        resolve(this.consultation);
                    })
                    .catch((error) => {
                        console.log('error', error.response.status);
                        reject(error);
                        if (error.response && error.response.status === 403) {
                            router.push({ name: 'view' });
                        }
                    });
            });
        },
        get_case_review(patient_id) {
            this.case_review = [];
            return new Promise((resolve, reject) => {
                axios
                    .get(`/api/documentation/case_review/${patient_id}`)
                    .then((response) => {
                        this.case_review = response.data;
                        resolve(this.case_review);
                    })
                    .catch((error) => {
                        console.log('error', error.response.status);
                        reject(error);
                        if (error.response && error.response.status === 403) {
                            router.push({ name: 'view' });
                        }
                    });
            });
        },
        get_individual_docu(patient_id) {
            this.patientDocu = [];
            axios
                .get(`/api/documentation/individual/${patient_id}`)
                .then((response) => {
                    this.patientDocu = response.data;
                })
                .catch((e) => {
                    console.error(e);
                });
        }
    }
});
