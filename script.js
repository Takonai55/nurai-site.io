// script.js

document.getElementById('orderForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Форманың жіберілуін тоқтату (бетті қайта жүктемеу үшін)

    // Пайдаланушыдан мәліметтерді алу
    const name = document.getElementById('name').value;
    const phone = document.getElementById('phone').value;
    const dish = document.getElementById('dish').value;
    const quantity = document.getElementById('quantity').value;

    // Мәліметтерді көрсететін хабарлама
    alert(`Тапсырыс қабылданды:
    Аты-жөні: ${name}
    Телефон: ${phone}
    Тағам: ${dish}
    Мөлшер: ${quantity} дана`);

    // Форма мәліметтерін тазарту
    document.getElementById('orderForm').reset();
});
