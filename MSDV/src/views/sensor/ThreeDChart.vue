<template>
    <div
        class="dark:bg-slate-400"
        ref="chartContainer"
        style="width: 1000px; height: 600px"
    ></div>
</template>

<script>
import { init } from 'echarts';
import 'echarts-gl';

export default {
    props: {
        thumbPoints: {
            type: Array,
            required: true
        },
        digitPoints: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
            chart: null
        };
    },
    mounted() {
        if (!this.thumbPoints.length || !this.digitPoints.length) {
            console.error('Thumb Points or Digit Points are empty');
            return;
        }

        this.chart = init(this.$refs.chartContainer);

        const option = {
            tooltip: {
                formatter: (params) => {
                    return `${params.seriesName}<br/>X: ${params.data.value[0]}<br/>Y: ${params.data.value[1]}<br/>Z: ${params.data.value[2]}`;
                }
            },
            legend: {
                data: ['Thumb', 'Digit']
            },
            visualMap: {
                show: false,
                dimension: 2,
                min: 0,
                max: 30
            },
            xAxis3D: {
                type: 'value',
                name: 'X-axis'
            },
            yAxis3D: {
                type: 'value',
                name: 'Y-axis'
            },
            zAxis3D: {
                type: 'value',
                name: 'Z-axis'
            },
            grid3D: {
                boxWidth: 100,
                boxHeight: 100,
                boxDepth: 100,
                axisPointer: {
                    show: true
                },
                projection: 'perspective',
                alpha: 20,
                beta: 30,
                light: {
                    main: {
                        intensity: 1.5
                    }
                }
            },
            series: [
                {
                    name: 'Thumb',
                    type: 'line3D',
                    data: this.thumbPoints.map((point) => {
                        return {
                            value: [point.x, point.y, point.z],
                            name: point.name,
                            lineStyle: {
                                color: '#0e7490'
                            }
                        };
                    }),
                    lineStyle: {
                        color: '#0e7490',
                        width: 4
                    }
                },
                {
                    name: 'Digit',
                    type: 'line3D',
                    data: this.digitPoints.map((point) => {
                        return {
                            value: [point.x, point.y, point.z],
                            name: point.name,
                            lineStyle: {
                                color: '#7e22ce'
                            }
                        };
                    }),
                    lineStyle: {
                        color: '#7e22ce',
                        width: 4
                    }
                }
            ]
        };

        this.chart.setOption(option);
    },
    beforeDestroy() {
        if (this.chart) {
            this.chart.dispose();
        }
    }
};
</script>
