// static/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    const globalMessageArea = document.getElementById('global-message-area');

    function displayToastMessage(message, type = 'info') {
        const globalMessageArea = document.getElementById('global-message-area');
        if (!globalMessageArea) return;
        // Remove any existing toast messages
        globalMessageArea.querySelectorAll('.toast-message').forEach(el => el.remove());

        const toast = document.createElement('div');
        toast.className = `toast-message toast-${type}`;
        toast.textContent = message;
        globalMessageArea.appendChild(toast);
        requestAnimationFrame(() => toast.classList.add('show'));
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    }

    // Mobile menu toggle (if not already in base.html or if more complex logic needed)
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', () => {
            const expanded = mobileMenuButton.getAttribute('aria-expanded') === 'true' || false;
            mobileMenuButton.setAttribute('aria-expanded', !expanded);
            mobileMenu.classList.toggle('hidden');
            const icon = mobileMenuButton.querySelector('i');
            icon.classList.toggle('fa-bars');
            icon.classList.toggle('fa-times');
        });
    }
    
    // Enhance park card image loading
    const parkImages = document.querySelectorAll('.park-card img');
    parkImages.forEach(img => {
        img.loading = 'lazy';
        img.onerror = () => {
            const parkName = img.alt.replace('Image of ', '');
            handleImageError(img, parkName);
        };
    });
}); // <-- Ensure this closing brace and parenthesis is present

// Add image handling functions
async function handleImageError(img, parkName) {
    try {
        const response = await fetch(`/api/fallback-image?park=${encodeURIComponent(parkName)}`);
        if (!response.ok) throw new Error('Failed to get fallback image');
        
        const data = await response.json();
        if (data.url) {
            img.src = data.url;
            return;
        }
        throw new Error('No fallback image URL');
    } catch (error) {
        console.error('Image fallback error:', error);
        img.src = '/static/img/default-park.jpg';
    }
}