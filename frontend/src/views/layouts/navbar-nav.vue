<template>
  <nav class="greedys sidebar-horizantal">
      <ul class="list-inline-item list-unstyled links sidebar-horizantal">
          <template v-for="item in sideBarData" :key="item.title">
              <li class="menu-title">
                  <span>{{ item.title }}</span>
              </li>
              <template v-for="menu in item.menu" :key="menu.menuValue">
                  <li v-if="!menu.hasSubRoute">
                      <router-link :to="menu.route">
                          <i :class="'feather feather-' + menu.icon"></i>
                          <span>{{ menu.menuValue }}</span>
                      </router-link>
                  </li>
                  <li class="submenu" v-if="menu.hasSubRoute" @click="expandSubMenus(menu)">
                      <a href="javascript:void(0)" :class="{ subdrop: menu.showSubRoute }">
                          <i :class="'feather feather-' + menu.icon"></i>
                          <span>{{ menu.menuValue }}</span>
                          <span class="menu-arrow"></span>
                      </a>
                      <ul :class="{ 'd-block': menu.showSubRoute, 'd-none': !menu.showSubRoute }">
                          <template v-for="subMenu in menu.subMenus" :key="subMenu.menuValue">
                              <li>
                                  <router-link :to="subMenu.route">{{ subMenu.menuValue }}</router-link>
                              </li>
                          </template>
                      </ul>
                  </li>
              </template>
          </template>
      </ul>
      <button @click="openMoreMenus" class="viewmoremenu">
          {{ showMoreMenu ? 'Less Menu' : 'More Menu' }}
      </button>
      <!-- Hidden Menu Items -->
      <ul class="hidden-links" :class="{ hidden: showMoreMenu === false }">
          <template v-for="item in sideBarData" :key="item.title">
              <li class="menu-title">
                  <span>{{ item.title }}</span>
              </li>
              <template v-for="menu in item.menu" :key="menu.menuValue">
                  <li v-if="!menu.hasSubRoute && !isMainMenuItem(menu.menuValue)">
                      <router-link :to="menu.route">
                          <i :class="'feather feather-' + menu.icon"></i>
                          <span>{{ menu.menuValue }}</span>
                      </router-link>
                  </li>
                  <li class="submenu" 
                      v-if="menu.hasSubRoute && !isMainMenuItem(menu.menuValue)"
                      @click="expandSubMenus(menu)">
                      <a href="javascript:void(0)" :class="{ subdrop: menu.showSubRoute }">
                          <i :class="'feather feather-' + menu.icon"></i>
                          <span>{{ menu.menuValue }}</span>
                          <span class="menu-arrow"></span>
                      </a>
                      <ul :class="{ 'd-block': menu.showSubRoute, 'd-none': !menu.showSubRoute }">
                          <template v-for="subMenu in menu.subMenus" :key="subMenu.menuValue">
                              <li>
                                  <router-link :to="subMenu.route">{{ subMenu.menuValue }}</router-link>
                              </li>
                          </template>
                      </ul>
                  </li>
              </template>
          </template>
      </ul>
  </nav>
</template>

<script>
import sideBarData from "@/assets/json/sidebar-data.json";

export default {
  data() {
      return {
          sideBarData: sideBarData,
          showMoreMenu: false,
          mainMenuItems: ['Dashboard', 'Accounts', 'Transfers'] // Items to show in main menu
      };
  },
  methods: {
      expandSubMenus(menu) {
          this.sideBarData.forEach((item) => {
              item.menu.forEach((subMenu) => {
                  if (subMenu !== menu) {
                      subMenu.showSubRoute = false;
                  }
              });
          });
          menu.showSubRoute = !menu.showSubRoute;
      },
      openMoreMenus() {
          this.showMoreMenu = !this.showMoreMenu;
      },
      isMainMenuItem(menuValue) {
          return this.mainMenuItems.includes(menuValue);
      }
  }
};
</script>

<style>
/* Add your styles here */
</style>