from app.apis import SignupAPI, LoginAPI, ProfileAPI

urls = {
    'signup/': SignupAPI,
    'login/': LoginAPI,
    'profile/': ProfileAPI,
}
