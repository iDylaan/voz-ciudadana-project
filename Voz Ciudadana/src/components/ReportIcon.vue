<script setup>
import { defineProps, computed } from 'vue';

// Definimos los props que va a recibir el componente
const props = defineProps({
    iconColor: {
        type: String,
        default: '#000000'
    },
    iconSize: {
        type: Number,
        default: 24
    },
    iconValue: {
        type: String,
        default: "no-icon"
    }
});

const iconStyle = computed(() => {
    return {
        color: props.iconColor,
        fill: props.iconColor,
        width: `${props.iconSize}px`,
        height: `${props.iconSize}px`
    }
})

const iconValues = [
    "bache",
    "basura",
    "coladera",
    "iluminacion",
    "inundacion",
    "mal_olor",
    "no-icon",
    "obstruccion",
    "poste",
    "semaforo",
    "sin_senial",
];


</script>

<template>
    <div class="icon">

        <svg :style="iconStyle" v-show="iconValue === iconValues[0]" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="512"
            height="512" x="0" y="0" viewBox="0 0 24 24" style="enable-background:new 0 0 512 512" xml:space="preserve">
            <g>
                <path
                    d="M23.784 23.621A1 1 0 0 1 23 24h-8a1 1 0 0 1-.97-1.245c1.231-4.947 8.773-4.935 9.943.016a1 1 0 0 1-.189.85Zm-4.7-18.078-3.819-3.476a5 5 0 0 0-4.958-.7L3.2 4.138A5.012 5.012 0 0 0 .125 8.106C.121 8.143 0 13.385 0 13.385c0 .217.006.489.022.788l19.8-7.911a5.442 5.442 0 0 0-.739-.719Zm-1.96 10.418A2 2 0 0 0 20.8 14.4l-.072-.177a3.992 3.992 0 0 0 .976-4.42l-.53-1.3c-.074-.184-.164-.353-.249-.527l-3.683 1.469.381.937a1 1 0 1 1-1.853.753l-.385-.948-9.519 3.805.363.915a1 1 0 0 1-1.858.738l-.362-.911-3.683 1.472a5.3 5.3 0 0 0 .189.575l.529 1.3a3.955 3.955 0 0 0 4.02 2.466l.083.2a2 2 0 0 0 3.707-1.5Z"
                    fill="currentColor" opacity="1" data-original="currentColor"></path>
            </g>
        </svg>

        <svg :style="iconStyle" v-show="iconValue === iconValues[1]" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="512"
            height="512" x="0" y="0" viewBox="0 0 512 512" style="enable-background:new 0 0 512 512" xml:space="preserve">
            <g>
                <path
                    d="M448 85.333h-66.133C371.66 35.703 328.002.064 277.333 0h-42.667c-50.669.064-94.327 35.703-104.533 85.333H64c-11.782 0-21.333 9.551-21.333 21.333S52.218 128 64 128h21.333v277.333C85.404 464.214 133.119 511.93 192 512h128c58.881-.07 106.596-47.786 106.667-106.667V128H448c11.782 0 21.333-9.551 21.333-21.333S459.782 85.333 448 85.333zM234.667 362.667c0 11.782-9.551 21.333-21.333 21.333-11.783 0-21.334-9.551-21.334-21.333v-128c0-11.782 9.551-21.333 21.333-21.333 11.782 0 21.333 9.551 21.333 21.333v128zm85.333 0c0 11.782-9.551 21.333-21.333 21.333-11.782 0-21.333-9.551-21.333-21.333v-128c0-11.782 9.551-21.333 21.333-21.333 11.782 0 21.333 9.551 21.333 21.333v128zM174.315 85.333c9.074-25.551 33.238-42.634 60.352-42.667h42.667c27.114.033 51.278 17.116 60.352 42.667H174.315z"
                    fill="currentColor" opacity="1" data-original="currentColor"></path>
            </g>
        </svg>

        <svg :style="iconStyle" v-show="iconValue === iconValues[2]" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="512"
            height="512" x="0" y="0" viewBox="0 0 24 24" style="enable-background:new 0 0 512 512" xml:space="preserve">
            <g>
                <path
                    d="M9.244 7.83a4.991 4.991 0 0 1 5.512 0l4.988-4.988a11.972 11.972 0 0 0-15.488 0ZM21.158 4.256 16.17 9.244a4.991 4.991 0 0 1 0 5.512l4.988 4.988a11.972 11.972 0 0 0 0-15.488ZM14.756 16.17a4.991 4.991 0 0 1-5.512 0l-4.988 4.988a11.972 11.972 0 0 0 15.488 0ZM7.83 14.756a4.991 4.991 0 0 1 0-5.512L2.842 4.256a11.972 11.972 0 0 0 0 15.488Z"
                    fill="currentColor" opacity="1" data-original="currentColor"></path>
            </g>
        </svg>

        <svg :style="iconStyle" v-show="iconValue === iconValues[3]" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="512"
            height="512" x="0" y="0" viewBox="0 0 24 24" style="enable-background:new 0 0 512 512" xml:space="preserve">
            <g>
                <path
                    d="M8 19.998h8v.31a3.694 3.694 0 0 1-3.69 3.69h-.619a3.694 3.694 0 0 1-3.69-3.69v-.31Zm13-11a8.991 8.991 0 0 1-3.068 6.763c-.739.648-1.275 1.413-1.594 2.237H7.563a6.84 6.84 0 0 0-1.695-2.417c-2.149-2.001-3.167-4.83-2.793-7.761C3.59 3.78 6.904.515 10.956.057a9.044 9.044 0 0 1 7.038 2.227A9.015 9.015 0 0 1 21 8.998ZM11 10a1 1 0 1 0 2 0V5a1 1 0 1 0-2 0v5Zm2.5 3.5a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 13.5 13.5Z"
                    fill="currentColor" opacity="1" data-original="#000000"></path>
            </g>
        </svg>

        <svg :style="iconStyle" v-show="iconValue === iconValues[4]" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="512"
            height="512" x="0" y="0" viewBox="0 0 24 24" style="enable-background:new 0 0 512 512" xml:space="preserve">
            <g>
                <path
                    d="M1 19.233a3 3 0 0 1 1.989.755.517.517 0 0 0 .211-.068A2.978 2.978 0 0 1 7 18.178v-.193a4.986 4.986 0 0 1 2.628-4.374c.05-.028.1-.056.152-.083a5.016 5.016 0 0 1 .576-.243c.135-.049.272-.091.413-.128s.311-.07.471-.1c.088-.014.17-.044.26-.053.154-.015.3-.018.455-.019h.063a5.005 5.005 0 0 1 .922.093c.034.007.068.01.1.017a4.974 4.974 0 0 1 .834.26c.038.015.076.029.114.046a5 5 0 0 1 .742.4l.111.074a5.038 5.038 0 0 1 .643.531l.093.094a5.16 5.16 0 0 1 .534.646l.068.1a5.12 5.12 0 0 1 .409.753c.013.032.024.064.037.1a5.01 5.01 0 0 1 .266.855.39.39 0 0 0 .011.067 5.008 5.008 0 0 1 .1.969v.192a2.982 2.982 0 0 1 3.8 1.743.478.478 0 0 0 .215.07 3.01 3.01 0 0 1 1.966-.765 2.9 2.9 0 0 1 1.02.192v-7.558a2 2 0 0 0-.563-1.392l-8.5-9.187a4 4 0 0 0-5.653-.223 4.244 4.244 0 0 0-.222.223L.581 10.469A2 2 0 0 0 0 11.879v7.542a2.971 2.971 0 0 1 1-.188Z"
                    fill="currentColor" opacity="1" data-original="currentColor"></path>
                <path
                    d="M9.227 19.917A2.92 2.92 0 0 1 12 18a3 3 0 0 1 2.8 1.934.565.565 0 0 0 .2.033v-1.982a3 3 0 0 0-6 0v1.982a.455.455 0 0 0 .227-.05ZM21 24a4.375 4.375 0 0 1-3-1.225 4.336 4.336 0 0 1-6 0 4.336 4.336 0 0 1-6 0 4.186 4.186 0 0 1-5.668.2 1 1 0 1 1 1.335-1.489 2.2 2.2 0 0 0 3.39-.822A1 1 0 0 1 6 20a1 1 0 0 1 .943.667 2.278 2.278 0 0 0 4.114 0A1 1 0 0 1 12 20a1 1 0 0 1 .943.667 2.278 2.278 0 0 0 4.114 0A1 1 0 0 1 18 20a1 1 0 0 1 .943.667 2.2 2.2 0 0 0 3.389.823 1 1 0 0 1 1.336 1.487A3.981 3.981 0 0 1 21 24Z"
                    fill="currentColor" opacity="1" data-original="currentColor"></path>
            </g>
        </svg>

        <svg :style="iconStyle" v-show="iconValue === iconValues[5]" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="512"
            height="512" x="0" y="0" viewBox="0 0 24 24" style="enable-background:new 0 0 512 512" xml:space="preserve"
            class="">
            <g>
                <path
                    d="M6.5 13h-5a1.5 1.5 0 0 1 0-3h5a1.5 1.5 0 0 1 0 3ZM18.5 13h-7a1.5 1.5 0 0 1 0-3h7A2.5 2.5 0 0 0 21 7.468a2.031 2.031 0 0 0-1.656-1.941A2 2 0 0 0 17 7.5 1.5 1.5 0 0 1 15.5 9c-2.767-.318-1.178-4.225.26-5.308A5 5 0 0 1 24 7.431 5.5 5.5 0 0 1 18.5 13ZM7 8H1.5a1.5 1.5 0 0 1 0-3H7a1.069 1.069 0 0 0 1.075-.777.982.982 0 0 0-.208-.818 1.158 1.158 0 0 0-1.681.088A1.5 1.5 0 1 1 3.859 1.6a4.125 4.125 0 0 1 6.307-.116 3.989 3.989 0 0 1 .858 3.275A4.031 4.031 0 0 1 7 8ZM15.585 24.008a4.832 4.832 0 0 1-3.709-1.752 1.5 1.5 0 0 1 2.323-1.9 1.736 1.736 0 0 0 2.542.11 1.508 1.508 0 0 0 .322-1.256A1.606 1.606 0 0 0 15.438 18H1.5a1.5 1.5 0 0 1 0-3h13.938a4.577 4.577 0 0 1 4.577 3.678 4.506 4.506 0 0 1-4.43 5.33Z"
                    fill="currentColor" opacity="1" data-original="currentColor"></path>
            </g>
        </svg>

        <svg :style="iconStyle" v-show="iconValue === iconValues[6]" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="512"
            height="512" x="0" y="0" viewBox="0 0 24 24" style="enable-background:new 0 0 512 512" xml:space="preserve">
            <g>
                <path
                    d="M12 0a12 12 0 1 0 12 12A12.013 12.013 0 0 0 12 0Zm0 20a1 1 0 1 1 1-1 1 1 0 0 1-1 1Zm1.93-7.494a1.982 1.982 0 0 0-.93 1.751V15a1 1 0 0 1-2 0v-.743a3.954 3.954 0 0 1 1.964-3.5 2 2 0 0 0 1-2.125 2.024 2.024 0 0 0-1.6-1.595A2 2 0 0 0 10 9a1 1 0 0 1-2 0 4 4 0 1 1 5.93 3.505Z"
                    fill="currentColor" opacity="1" data-original="currentColor"></path>
            </g>
        </svg>

        <svg :style="iconStyle" v-show="iconValue === iconValues[7]" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="512"
            height="512" x="0" y="0" viewBox="0 0 24 24" style="enable-background:new 0 0 512 512" xml:space="preserve"
            class="">
            <g>
                <path
                    d="M24 23a1 1 0 0 1-1 1H1a1 1 0 1 1 0-2h.873l1.469-4h17.316l1.469 4H23a1 1 0 0 1 1 1Zm-5.913-12H5.913l-1.837 5h15.847l-1.837-5Zm-.735-2-2.579-7.021C14.341.805 13.252.045 12 .045s-2.341.76-2.773 1.936l-2.579 7.02h10.704Z"
                    fill="currentColor" opacity="1" data-original="currentColor"></path>
            </g>
        </svg>

        <svg :style="iconStyle" v-show="iconValue === iconValues[8]" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="512"
            height="512" x="0" y="0" viewBox="0 0 24 24" style="enable-background:new 0 0 512 512" xml:space="preserve">
            <g>
                <path
                    d="M22.5 0A1.5 1.5 0 0 0 21 1.5V2h-1v-.5a1.5 1.5 0 1 0-3 0V2h-3.5v-.5a1.5 1.5 0 1 0-3 0V2H7v-.5a1.5 1.5 0 1 0-3 0V2H3v-.5a1.5 1.5 0 1 0-3 0v1C0 3.878 1.122 5 2.5 5h1.379l6.621 6.621V22.5a1.5 1.5 0 1 0 3 0V11.621L20.121 5H21.5C22.878 5 24 3.878 24 2.5v-1A1.5 1.5 0 0 0 22.5 0ZM8.121 5H10.5v2.379L8.121 5ZM13.5 5h2.379L13.5 7.379V5Z"
                    fill="currentColor" opacity="1" data-original="currentColor"></path>
            </g>
        </svg>

        <svg :style="iconStyle" v-show="iconValue === iconValues[9]" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="512"
            height="512" x="0" y="0" viewBox="0 0 24 24" style="enable-background:new 0 0 512 512" xml:space="preserve"
            class="">
            <g>
                <path
                    d="M15 0H9C6.243 0 4 2.243 4 5v14c0 2.757 2.243 5 5 5h6c2.757 0 5-2.243 5-5V5c0-2.757-2.243-5-5-5Zm-3 22c-1.654 0-3-1.346-3-3s1.346-3 3-3 3 1.346 3 3-1.346 3-3 3Zm0-7c-1.654 0-3-1.346-3-3s1.346-3 3-3 3 1.346 3 3-1.346 3-3 3Zm0-7c-1.654 0-3-1.346-3-3s1.346-3 3-3 3 1.346 3 3-1.346 3-3 3Z"
                    fill="currentColor" opacity="1" data-original="currentColor"></path>
            </g>
        </svg>

        <svg :style="iconStyle" v-show="iconValue === iconValues[10]" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="512"
            height="512" x="0" y="0" viewBox="0 0 24 24" style="enable-background:new 0 0 512 512" xml:space="preserve"
            class="">
            <g>
                <path
                    d="M23.707 23.707a.999.999 0 0 1-1.414.001l-21.999-22A1 1 0 1 1 1.708.293l11.293 11.313V6.001a2 2 0 1 1 4 0v9.598l2 1.996V2a2 2 0 1 1 4 0v19.588l.705.705a1 1 0 0 1 .002 1.414ZM3 17a2 2 0 0 0-2 2v3a2 2 0 1 0 4 0v-3a2 2 0 0 0-2-2Zm6 7a2 2 0 0 0 2-2v-6.739l-4-3.993v10.731a2 2 0 0 0 2 2Zm6 0a2 2 0 0 0 2-2v-.749l-4-3.993V22a2 2 0 0 0 2 2Z"
                    fill="currentColor" opacity="1" data-original="currentColor" class=""></path>
            </g>
        </svg>

    </div>
</template>

<style lang="scss" scoped></style>