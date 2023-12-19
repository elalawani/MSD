import { defineStore } from 'pinia';
import axios from 'axios';

export const useConversationStore = defineStore({
    id: 'conversation',
    state: () => ({
        conversations: []
    }),
    actions: {
        async getConversation() {
            this.conversations = [];
            await axios
                .get(`/api/conversation/`)
                .then((response) => {
                    this.conversations = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        }
    }
});
