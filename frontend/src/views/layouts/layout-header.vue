<template>
  <div class="header header-one">
    <router-link
      to="/dashboard/"
      class="d-inline-flex d-sm-inline-flex align-items-center d-md-inline-flex d-lg-none align-items-center device-logo"
    >
      <img src="@/assets/img/salaam_logo.png" class="img-fluid logo2" alt="Logo" />
    </router-link>
    <div
      class="main-logo d-inline float-start d-lg-flex align-items-center d-none d-sm-none d-md-none"
    >
      <div class="logo-white">
        <router-link to="/dashboard/">
          <img
            src="@/assets/img/salaam_logo.png"
            class="img-fluid logo-blue"
            alt="Logo"
          />
        </router-link>
        <router-link to="/dashboard/">
          <img
            src="@/assets/img/salaam_logo.png"
            class="img-fluid logo-small"
            alt="Logo"
          />
        </router-link>
      </div>
      <div class="logo-color">
        <router-link to="/dashboard/">
          <img src="@/assets/img/salaam_logo.png" class="img-fluid logo-blue" alt="Logo" />
        </router-link>
        <router-link to="/dashboard/">
          <img
            src="@/assets/img/salaam_logo.png"
            class="img-fluid logo-small"
            alt="Logo"
          />
        </router-link>
      </div>
    </div>

    <!-- Sidebar Toggle -->
    <a href="javascript:void(0);" id="toggle_btn" @click="toggleSidebar">
      <span class="toggle-bars">
        <span class="bar-icons"></span>
        <span class="bar-icons"></span>
        <span class="bar-icons"></span>
        <span class="bar-icons"></span>
      </span>
    </a>
    <!-- /Sidebar Toggle -->

    <!-- Search -->
    <!-- <div class="top-nav-search">
      <form>
        <input type="text" class="form-control" placeholder="Search here" />
        <button class="btn" type="submit">
          <img src="@/assets/img/icons/search.svg" alt="img" />
        </button>
      </form>
    </div> -->
    <!-- /Search -->

    <!-- Mobile Menu Toggle -->
    <a class="mobile_btn" id="mobile_btn" @click="toggleSidebar1">
      <i class="fas fa-bars"></i>
    </a>
    <!-- /Mobile Menu Toggle -->

    <!-- Header Menu -->
    <ul class="nav nav-tabs user-menu">
      <!-- Flag -->
      <li class="nav-item dropdown has-arrow flag-nav">
        <a
          class="nav-link dropdown-toggle"
          data-bs-toggle="dropdown"
          href="javascript:;"
          role="button"
        >
          <img src="@/assets/img/flags/us1.png" alt="flag" /><span>English</span>
        </a>
        <div class="dropdown-menu dropdown-menu-end">
          <a href="javascript:void(0);" class="dropdown-item">
            <img src="@/assets/img/flags/us.png" alt="flag" /><span>English</span>
          </a>
        </div>
      </li>
      <!-- /Flag -->

      <!-- <li class="nav-item has-arrow dropdown-heads">
        <a href="javascript:void(0);" class="toggle-switch">
          <i class="feather feather-moon"></i>
        </a>
      </li> -->
      <li class="nav-item dropdown flag-nav dropdown-heads">
        <a class="nav-link" data-bs-toggle="dropdown" href="javascript:;" role="button">
          <i
            class="feather feather-bell d-flex align-items-center justify-content-center"
          ></i>
          <span class="badge rounded-pill"></span>
        </a>
        <div class="dropdown-menu notifications">
          <div class="topnav-dropdown-header">
            <div class="notification-title">
              Notifications <router-link to="/notifications">View all</router-link>
            </div>
            <a href="javascript:void(0)" class="clear-noti d-flex align-items-center"
              >Mark all as read <i class="feather feather-check-circle"></i
            ></a>
          </div>
          <div class="noti-content">
            <ul class="notification-list">
              <li class="notification-message">
                <router-link to="/profile">
                  <div class="d-flex">
                    <span class="avatar avatar-md active">
                      <img
                        class="avatar-img rounded-circle"
                        alt="avatar-img"
                        src="@/assets/img/profiles/avatar-02.jpg"
                      />
                    </span>
                    <div class="media-body">
                      <p class="noti-details">
                        <span class="noti-title">---</span> ---
                        <span class="noti-title">---</span>
                      </p>
                      
                      <p class="noti-time">
                        <span class="notification-time">-----</span>
                      </p>
                    </div>
                  </div>
                </router-link>
              </li>
            </ul>
          </div>
          <div class="topnav-dropdown-footer">
            <a href="javascript:;">Clear All</a>
          </div>
        </div>
      </li>
      <li class="nav-item has-arrow dropdown-heads">
        <a href="javascript:void(0);" class="win-maximize" @click="initFullScreen">
          <i
            class="feather feather-maximize d-flex align-items-center justify-content-center"
          ></i>
        </a>
      </li>
      <!-- User Menu -->
      <li class="nav-item dropdown">
        <a href="javascript:void(0)" class="user-link nav-link" data-bs-toggle="dropdown">
          <span class="user-img">
            <img
              :src="'@assets/img/profiles/avatar-07.jpg'"
              alt="img"
              class="profilesidebar"
            />
            <span class="animate-circle"></span>
          </span>
          <span class="user-content">
            <span class="user-details">{{ user.role }}</span>
            <span class="user-name">{{ user.name }}</span>
          </span>
        </a>
        <div class="dropdown-menu menu-drop-user">
          <div class="profilemenu">
            <div class="subscription-menu">
              <ul>
                <li>
                  <router-link class="dropdown-item" to="/profile">Profile</router-link>
                </li>
              </ul>
            </div>
            <div class="subscription-logout">
              <ul>
                <li class="pb-0">
                  <a class="dropdown-item" href="javascript:void(0)" @click="logout">Log Out</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </li>
      <!-- /User Menu -->
    </ul>

    <!-- /Header Menu -->
  </div>

  <side-settings></side-settings>
</template>

<script>
import { useAuthStore } from '@/stores/auth'

export default {
  data() {
    return {
      user: {
        name: '',
        role: '',
        avatar: ''
      }
    };
  },
  mounted() {
    // Add click event listener
    this.$nextTick(() => {
      document.addEventListener("click", this.handleToggleClick);
    });

    // Get user data from auth store
    const authStore = useAuthStore()
    this.user = {
      name: authStore.user?.first_name + ' ' + authStore.user?.last_name || 'John Smith',
      role: authStore.user?.email || '--',
      avatar: authStore.user?.avatar || null
    }

    // Add mouseover event listener
    document.addEventListener("mouseover", (event) => {
      event.stopPropagation();

      var body = document.body;
      var toggleBtn = document.getElementById("toggle_btn");
      // var sidebar = document.getElementsByClassName("sidebar")[0];
      var subdropUL = document.getElementsByClassName("subdrop");

      if (body.classList.contains("mini-sidebar") && toggleBtn.style.display !== "none") {
        var target = event.target.closest(".sidebar");

        if (target) {
          body.classList.add("expand-menu");
          for (var i = 0; i < subdropUL.length; i++) {
            var ul = subdropUL[i].nextElementSibling;
            if (ul) {
              ul.style.display = "block";
            }
          }
        } else {
          body.classList.remove("expand-menu");
          for (var i = 0; i < subdropUL.length; i++) {
            var ul = subdropUL[i].nextElementSibling;
            if (ul) {
              ul.style.display = "none";
            }
          }
        }

        event.preventDefault();
      }
    });
  },
  beforeUnmount() {
    document.removeEventListener("click", this.handleToggleClick);
  },

  methods: {
    toggleSidebar1() {
      const body = document.body;
      body.classList.toggle("slide-nav");
    },
    toggleSidebar() {
      const body = document.body;
      body.classList.toggle("mini-sidebar");
    },
    initFullScreen() {
      document.body.classList.toggle("fullscreen-enable");
      if (
        !document.fullscreenElement &&
        /* alternative standard method */
        !document.mozFullScreenElement &&
        !document.webkitFullscreenElement
      ) {
        // current working methods
        if (document.documentElement.requestFullscreen) {
          document.documentElement.requestFullscreen();
        } else if (document.documentElement.mozRequestFullScreen) {
          document.documentElement.mozRequestFullScreen();
        } else if (document.documentElement.webkitRequestFullscreen) {
          document.documentElement.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT);
        }
      } else {
        if (document.cancelFullScreen) {
          document.cancelFullScreen();
        } else if (document.mozCancelFullScreen) {
          document.mozCancelFullScreen();
        } else if (document.webkitCancelFullScreen) {
          document.webkitCancelFullScreen();
        }
      }
    },
    async logout() {
      const authStore = useAuthStore()
      await authStore.logout()
      this.$router.push('/login')
    }
  },
};
</script>
