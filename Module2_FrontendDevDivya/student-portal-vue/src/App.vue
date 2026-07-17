<template>
  <main>
  <nav aria-label="Main navigation">
    <RouterLink to="/">Home</RouterLink> |
    <RouterLink to="/courses">Courses</RouterLink> |
    <RouterLink to="/profile">Profile</RouterLink>
  </nav>

  <RouterView />
  </main>
</template>