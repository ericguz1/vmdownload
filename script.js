function downloadFile(fileName) {
    const link = document.createElement('a');
    link.href = fileName; // Ensure the path includes the folder name
    link.download = fileName.split('/').pop(); // Get the file name
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
