<template>
    <div class="flex flex-col p-4 space-y-4 justify-around w-full">
        <div class="flex flex-col">
            <div class="mb-4">
                <div class="text-xl font-bold p-2">Evaluation</div>
                <div v-if="outFileData.status" class="font-bold">
                    Patient Staus:
                    <span class="font-light pl-2">
                        {{ outFileData.status }} von 5</span
                    >
                </div>
                <div v-if="outFileData.movement" class="font-bold">
                    Finger Bewegung:
                    <span class="font-light pl-2">
                        {{ outFileData.movement }} von 5</span
                    >
                </div>
            </div>
            <div class="text-xl font-bold">file informations:</div>
            <div class="flex flex-col mt-2 ml-4">
                <div v-if="outFileData.uploaded_at" class="font-bold">
                    hochgeladen am:
                    <span class="font-light pl-2">{{
                        dateTime(outFileData.uploaded_at)
                    }}</span>
                </div>
            </div>
        </div>
        <div class="flex flex-col">
            <div class="text-xl font-bold">Allgemeine Daten:</div>
            <div class="flex flex-col mt-2 ml-4">
                <div v-if="moreInfo.resourceType" class="font-bold">
                    resource:
                    <span class="font-light pl-2">{{
                        moreInfo.resourceType
                    }}</span>
                </div>
                <div v-if="moreInfo.status" class="font-bold">
                    status:
                    <span class="font-light pl-2">{{ moreInfo.status }}</span>
                </div>
                <div v-if="moreInfo.id" class="font-bold">
                    id: <span class="font-light pl-2">{{ moreInfo.id }}</span>
                </div>
            </div>
        </div>
        <div class="flex flex-col">
            <div class="text-xl font-bold">Textuelle Zusammenfassung:</div>
            <div class="flex flex-col mt-2 ml-4">
                <div v-if="moreInfo.text.div " class="font-bold">
                    text:
                    <div class="font-light pl-2">{{ moreInfo.text.div }}</div>
                    <div class="font-light pl-2">
                        {{ moreInfo.text.status }}
                    </div>
                </div>
            </div>
        </div>
        <div class="flex flex-col">
            <div class="text-xl font-bold">Code-Informationen:</div>
            <div class="flex flex-col mt-2 ml-4">
                <div v-if="moreInfo.code" class="font-bold">
                    code:
                    <span class="font-light pl-2">{{
                        moreInfo.code.coding[0].code
                    }}</span>
                </div>
                <div v-if="moreInfo.code" class="font-bold">
                    system:
                    <span class="font-light pl-2">{{
                        moreInfo.code.coding[0].system
                    }}</span>
                </div>
                <div v-if="moreInfo.code" class="font-bold">
                    display:
                    <span class="font-light pl-2">{{
                        moreInfo.code.coding[0].display
                    }}</span>
                </div>
            </div>
        </div>
        <div class="flex flex-col">
            <div class="text-xl font-bold">Komponenten der Beobachtung:</div>
            <div
                    v-if="allData.code"
                v-for="(data, index) in allData.code.coding"
                :key="index"
                class="flex flex-col mt-2 ml-4"
            >
                <div class="font-bold">
                    display:
                    <span class="font-light pl-2">{{ data.display }}</span>
                </div>
                <div class="font-bold">
                    system:
                    <span class="font-light pl-2">{{ data.system }}</span>
                </div>
                <div class="font-bold">
                    code:
                    <span class="font-light pl-2">{{ data.code }}</span>
                </div>
                <div class="font-bold">
                    Sampled Data:
                    <span class="font-light pl-2">Sehe Chart</span>
                </div>
                <div class="font-bold">
                    dimensions:
                    <span class="font-light pl-2">{{
                        allData.valueSampledData.dimensions
                    }}</span>
                </div>
                <div class="font-bold">
                    period:
                    <span class="font-light pl-2">{{
                        allData.valueSampledData.period
                    }}</span>
                </div>
                <div class="font-bold">
                    origin:
                    <span class="font-light pl-2">{{
                        allData.valueSampledData.origin.value
                    }}</span>
                </div>
            </div>
        </div>
        <div class="flex flex-col">
            <div  class="text-xl font-bold">Durchführender Arzt:</div>
            <div class="flex flex-col mt-2 ml-4">
                <div v-if="moreInfo.performer" class="font-bold">
                    performer:
                    <span class="font-light pl-2">{{
                        moreInfo.performer[0].display
                    }}</span>
                </div>
            </div>
        </div>
        <div class="flex flex-col">
            <div class="text-xl font-bold">Zeitpunkt der Beobachtung:</div>
            <div class="flex flex-col mt-2 ml-4">
                <div v-if="moreInfo.effectiveDateTime" class="font-bold">
                    effectiveDateTime:
                    <span class="font-light pl-2">{{
                        moreInfo.effectiveDateTime
                    }}</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import dateTime from '../../setUp/global/date-filter';

export default {
    name: 'informationView',
    methods: { dateTime },
    props: {
        allData: {
            type: Object,
            required: true
        },
        moreInfo: {
            type: Object,
            required: true
        },
        outFileData: {
            type: Object,
            required: true
        }
    }
};
</script>
