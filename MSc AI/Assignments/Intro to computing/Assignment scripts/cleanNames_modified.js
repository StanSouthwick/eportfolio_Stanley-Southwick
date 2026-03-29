// cleanNames.js

// Function to process a list of names: remove duplicates, sort alphabetically, and convert to uppercase
function processNames(names) {
    let namesNew = names.map((name) => name.toUpperCase()); // Convert all names to uppercase for consistency
    let uniqueNames = [...new Set(namesNew)]; // removes duplicates
    uniqueNames.sort(); // sorts alphabetically
    return uniqueNames;
}

// Test list with duplicates and inconsistent capitalisation
const testNames = ["Alice", "bob", "alice", "Charlie", "BOB", "dave", "Eve", "charlie"];

console.log("Original list:", testNames);
console.log("Processed list:", processNames(testNames));