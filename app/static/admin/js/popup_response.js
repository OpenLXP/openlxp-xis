<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> dcb09cd (Testing Jack's ability to commit changes)
/*global opener */
'use strict';
{
    const initData = JSON.parse(document.getElementById('django-admin-popup-response-constants').dataset.popupResponse);
    switch(initData.action) {
    case 'change':
        opener.dismissChangeRelatedObjectPopup(window, initData.value, initData.obj, initData.new_value);
        break;
    case 'delete':
        opener.dismissDeleteRelatedObjectPopup(window, initData.value);
        break;
    default:
        opener.dismissAddRelatedObjectPopup(window, initData.value, initData.obj);
        break;
    }
}
<<<<<<< HEAD
=======
=======
>>>>>>> 68c08d4 (django project set up with docker and same api endpoint)
/*global opener */
'use strict';
{
    const initData = JSON.parse(document.getElementById('django-admin-popup-response-constants').dataset.popupResponse);
    switch(initData.action) {
    case 'change':
        opener.dismissChangeRelatedObjectPopup(window, initData.value, initData.obj, initData.new_value);
        break;
    case 'delete':
        opener.dismissDeleteRelatedObjectPopup(window, initData.value);
        break;
    default:
        opener.dismissAddRelatedObjectPopup(window, initData.value, initData.obj);
        break;
    }
}
<<<<<<< HEAD
>>>>>>> 86c1339 (django project set up with docker; sample api endpoint)
=======
>>>>>>> 68c08d4 (django project set up with docker and same api endpoint)
=======
>>>>>>> dcb09cd (Testing Jack's ability to commit changes)
