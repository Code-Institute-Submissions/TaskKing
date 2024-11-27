document.addEventListener('DOMContentLoaded', function() {
    const taskItems = document.querySelectorAll('.task-item');
    taskItems.forEach((item, index) => {
        item.style.animationDelay = `${index * 0.1}s`;
        item.classList.add('animate__animated', 'animate__fadeInUp');
    });
});