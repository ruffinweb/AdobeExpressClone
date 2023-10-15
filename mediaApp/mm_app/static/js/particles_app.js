//  This seems easier than changing the app.js file to only run these lines at the home route.
/* particlesJS.load(@dom-id, @path-json, @callback (optional)); */

particlesJS.load(particlesJsPath, particlesJsonPath, function() {
  console.log('callback - particles.js config loaded');
});
