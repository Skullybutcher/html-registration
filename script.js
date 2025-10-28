// Get references to all required elements
const form = document.getElementById('registration-form');
const successMessage = document.getElementById('success-message');
const errorMessage = document.getElementById('error-message');
const submitBtn = document.getElementById('submit-btn');
const downloadBtn = document.getElementById('download-btn');

// This variable will hold the validated data
let validData = null;

// --- Helper Function: Get Form Data ---
function getFormData() {
    const name = document.getElementById('name').value;
    const rollNumber = document.getElementById('roll-number').value;
    const college = document.getElementById('college').value;
    const branch = document.getElementById('branch').value;
    const email = document.getElementById('email').value;
    const mobile = document.getElementById('mobile').value;
    const genderRadio = document.querySelector('input[name="gender"]:checked');
    const gender = genderRadio ? genderRadio.value : '';
    const yearOfStudy = document.getElementById('year-of-study').value;

    return { name, rollNumber, college, branch, email, mobile, gender, yearOfStudy };
}

// --- Helper Function: Validate Data ---
function validateData(data) {
    // Check if any value in the data object is empty
    return Object.values(data).every(value => value.trim() !== '');
}

// --- Helper Function: Create CSV Content ---
function createCSV(data) {
    // CSV Header Row
    const csvHeader = "Name,Roll Number,College,Branch,Email,Mobile,Gender,Year of Study\n";
    
    // Function to escape commas/quotes
    const escapeCSV = (field) => {
        if (field === null || field === undefined) return '""';
        let str = String(field);
        if (str.includes(',') || str.includes('"') || str.includes('\n')) {
            return `"${str.replace(/"/g, '""')}"`;
        }
        return str;
    };

    // CSV Data Row from the data object
    const csvData = [
        escapeCSV(data.name),
        escapeCSV(data.rollNumber),
        escapeCSV(data.college),
        escapeCSV(data.branch),
        escapeCSV(data.email),
        escapeCSV(data.mobile),
        escapeCSV(data.gender),
        escapeCSV(data.yearOfStudy)
    ].join(',');
    
    return csvHeader + csvData;
}

// --- Helper Function: Trigger Download ---
function triggerDownload(csvContent) {
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-IS-1;' });
    const link = document.createElement('a');
    const url = URL.createObjectURL(blob);
    link.setAttribute('href', url);
    link.setAttribute('download', 'registration_details.csv');
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// --- Initial State ---
downloadBtn.disabled = true;

// --- Event Listener: Submit Button ---
submitBtn.addEventListener('click', function() {
    // Always hide messages on a new submit attempt
    successMessage.classList.add('hidden');
    errorMessage.classList.add('hidden');
    
    const data = getFormData();
    
    if (validateData(data)) {
        // Validation passed!
        validData = data; // Store the valid data
        successMessage.classList.remove('hidden');
        downloadBtn.disabled = false; // Enable download
        window.scrollTo(0, 0); // Scroll to top

        // Hide success message after 5 seconds
        setTimeout(() => {
            successMessage.classList.add('hidden');
        }, 5000);
    } else {
        // Validation failed!
        validData = null; // Clear any old valid data
        errorMessage.classList.remove('hidden');
        downloadBtn.disabled = true; // Ensure download is disabled
        window.scrollTo(0, 0);
    }
});

// --- Event Listener: Download Button ---
downloadBtn.addEventListener('click', function() {
    if (validData) {
        // If we have valid data, create CSV and trigger download
        const csvContent = createCSV(validData);
        triggerDownload(csvContent);
    } else {
        // This shouldn't happen if the button is disabled, but it's good practice
        console.error('No valid data to download.');
        errorMessage.classList.remove('hidden');
    }
});

// --- Event Listener: Form Input ---
// If the user changes any field, reset the state
form.addEventListener('input', function() {
    downloadBtn.disabled = true; // Disable download
    validData = null; // Invalidate old data
    successMessage.classList.add('hidden'); // Hide success message
    errorMessage.classList.add('hidden'); // Hide error message
});
