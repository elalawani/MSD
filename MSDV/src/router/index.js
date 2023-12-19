import { createRouter, createWebHistory } from 'vue-router';
import DashboardView from '@/views/DashboardView.vue';
import LoginView from '@/views/account/LoginView.vue';
import SignupView from '@/views/account/SignupView.vue';
import View from '@/views/patient/View.vue';
import createPatientView from '@/views/patient/CreatePatientView.vue';
import DetailView from '@/views/patient/DetailView.vue';
import PatientInfo from '@/views/patient/PatientInfo.vue';
import DocumentationView from '@/views/documentation/DocumentationView.vue';
import ConversationView from '@/views/conversation/ConversationView.vue';
import QuestionnaireView from '@/views/questionnaire/QuestionnaireView.vue';
import CreateBarthelIndexView from '@/views/questionnaire/creation/CreateBarthelIndexView.vue';
import TodoListView from '@/views/TodoListView.vue';
import ProfileView from '@/views/account/ProfileView.vue';
import CreateDocumentationView from '@/views/documentation/CreateDocumentationView.vue';
import ChartView from '@/views/sensor/ChartView.vue';
import NotFoundPage from '@/errors/templates/NotFoundPage.vue';
import NewDataFormView from '@/components/patient/sensor/view/NewDataFormView.vue';
const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            name: 'signup',
            path: '/signup',
            component: SignupView
        },
        {
            name: 'login',
            path: '/login',
            component: LoginView
        },
        {
            name: 'dashboard',
            path: '/',
            component: DashboardView
        },
        {
            name: 'profile',
            path: '/profile',
            component: ProfileView
        },
        {
            name: 'todolist',
            path: '/todolist',
            component: TodoListView
        },
        {
            name: 'view',
            path: '/view',
            component: View
        },
        {
            name: 'create_patient',
            path: '/create_patient',
            component: createPatientView
        },
        {
            name: 'details',
            path: '/details/:id',
            component: DetailView,
            meta: { requiresAuth: true },
            children: [
                {
                    name: 'patientInfo',
                    path: '/details/:id/info',
                    component: PatientInfo
                },
                {
                    name: 'chart',
                    path: '/details/:id/sensor',
                    component: ChartView
                },
                {
                    name: 'documentation',
                    path: '/details/:id/documentation',
                    component: DocumentationView
                },
                {
                    name: 'create_documentation',
                    path: '/details/:id/create_documentation',
                    component: CreateDocumentationView
                },
                {
                    name: 'conversation',
                    path: '/details/:id/conversation',
                    component: ConversationView
                },
                {
                    name: 'questionnaire',
                    path: '/details/:id/questionnaire',
                    component: QuestionnaireView
                },
                {
                    name: 'barthel',
                    path: '/details/:id/questionnaire/barthel',
                    component: CreateBarthelIndexView
                },
                {
                    path: '/details/:id/add_data',
                    name: 'add_data',
                    component: NewDataFormView,
                    meta: { requiresAuth: true }
                }
            ]
        },
        // template for errors
        {
            name: 'NotFoundPage',
            path: '/:pathMatch(.*)*',
            component: NotFoundPage
        }
    ]
});

export default router;
