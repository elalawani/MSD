import { library } from '@fortawesome/fontawesome-svg-core';

/* import specific icons */
import {
    faInfo,
    faArrowRight,
    faUser,
    faHouseChimney,
    faUsers,
    faMessage,
    faStethoscope,
    faEnvelope,
    faFemale,
    faMale,
    faLungs,
    faTemperatureHalf,
    faHeartbeat,
    faDroplet,
    faPaperPlane,
    faBookMedical
} from '@fortawesome/free-solid-svg-icons';
import {
    faTwitter,
    faYoutube,
    faLinkedin,
    faGithub
} from '@fortawesome/free-brands-svg-icons';

/* add icons to the library */
export default function setupFontawesome() {
    library.add(
        faArrowRight,
        faInfo,
        faUser,
        faUsers,
        faLinkedin,
        faStethoscope,
        faEnvelope,
        faMessage,
        faHouseChimney,
        faFemale,
        faMale,
        faYoutube,
        faTwitter,
        faGithub,
        faLungs,
        faTemperatureHalf,
        faHeartbeat,
        faDroplet,
        faPaperPlane,
        faBookMedical
    );
}
