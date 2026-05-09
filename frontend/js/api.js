// api.js
const BASE_URL = 'https://securify-production.up.railway.app';

export async function getDashboardData() {
    const response = await fetch(`${BASE_URL}/dashboard`);
    return await response.json();
}

export async function verifyFace(formData) {
    const response = await fetch(`${BASE_URL}/verify`, {
        method: 'POST',
        body: formData
    });
    return await response.json();
}