<template>
  <div class="page-header">
    <div class="content-page-header">
      <h5>{{ title }}</h5>
      <div class="list-btn">
        <ul class="filter-list">
          <li>
            <div class="short-filter">
              <img class="me-2" src="@/assets/img/icons/sort.svg" alt="Sort by select" />
              <div class="sort-by sort-by-ticket">
                <vue-select
                  :options="Permissionrole"
                  id="permissionrole"
                  placeholder="Sort by: Date"
                />
              </div>
            </div>
          </li>
          <li>
            <a
              class="btn btn-filters w-auto popup-toggle"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              data-bs-original-title="Filter"
              ><span class="me-2"
                ><img src="@/assets/img/icons/filter-icon.svg" alt="filter" /></span
              >Filter
            </a>
          </li>
          <li v-if="isRoleRoute">
            <a
              class="btn btn-primary"
              href="javascript:;"
              data-bs-toggle="modal"
              data-bs-target="#add_role"
              ><i class="fa fa-plus-circle me-2" aria-hidden="true"></i>{{ text }}</a
            >
          </li>
          <li v-if="isTicketRoute">
            <a
              class="btn btn-primary"
              href="javascript:;"
              data-bs-toggle="modal"
              data-bs-target="#add_ticket"
              ><i class="fa fa-plus-circle me-2" aria-hidden="true"></i>{{ text }}</a
            >
          </li>
          <li v-if="isTicketListRoute">
            <a
              class="btn btn-primary"
              href="javascript:;"
              data-bs-toggle="modal"
              data-bs-target="#add_ticket"
              ><i class="fa fa-plus-circle me-2" aria-hidden="true"></i>{{ text }}</a
            >
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    title: {
      type: String,
      default: "",
    },
    text: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      Permissionrole: ["Sort by: Date", "Sort by: Date 1", "Sort by: Date 2"],
    };
  },
  computed: {
    isRoleRoute() {
      return this.$route.path === "/roles-permission";
    },
    isTicketRoute() {
      return this.$route.path === "/tickets/all-tickets";
    },
    isTicketListRoute() {
      return this.$route.path === "/tickets/tickets-list";
    },
  },
};
</script>
