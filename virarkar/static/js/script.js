(() => {
    const root = document.documentElement;
    const toggle = document.querySelector('[data-theme-toggle]');
    const icon = document.querySelector('[data-theme-icon]');
    const label = document.querySelector('[data-theme-label]');

    if (!toggle) {
        return;
    }

    const updateToggle = (theme) => {
        const isDark = theme === 'dark';
        toggle.setAttribute('aria-pressed', String(isDark));
        toggle.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');

        if (icon) {
            icon.className = isDark ? 'bi bi-sun-fill' : 'bi bi-moon-stars-fill';
        }

        if (label) {
            label.textContent = isDark ? 'Light mode' : 'Dark mode';
        }
    };

    updateToggle(root.dataset.theme || 'light');

    toggle.addEventListener('click', () => {
        const nextTheme = root.dataset.theme === 'dark' ? 'light' : 'dark';
        root.dataset.theme = nextTheme;
        localStorage.setItem('virarkar-theme', nextTheme);
        updateToggle(nextTheme);
    });
})();
