<template>
    <button @mousedown="downloadFile">
        als {{ tagName }} laden &downarrow;
    </button>
</template>

<script>
import html2pdf from 'html2pdf.js';

export default {
    props: {
        dom: {
            type: String,
            required: true
        },
        name: {
            type: String,
            required: true
        },
        tagName: {
            type: String,
            required: true
        }
    },
    methods: {
        downloadFile() {
            const invoice = document.querySelector(this.dom);

            if (!invoice) {
                console.error('DOM element not found.');
                return;
            }

            const opt = {
                margin: 1,
                filename: this.name
            };

            html2pdf()
                .from(invoice)
                .set(opt)
                .save()
                .catch((error) => {
                    console.error('Error generating PDF:', error);
                });
        }
    }
};
</script>
