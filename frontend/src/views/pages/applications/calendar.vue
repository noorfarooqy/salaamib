<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <div class="page-header">
        <div class="content-page-header">
          <h5>Calendar</h5>
          <div class="list-btn">
            <ul class="filter-list">
              <li>
                <a href="javascript:;" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#add_event">Create
                  Event</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <!-- /Page Header -->

      <div class="row">
        <div class="col-lg-3 col-md-4">
          <div class="card">
            <div class="card-body">
              <h5 class="card-title mb-2">Drag & Drop Event</h5>
              <div id="calendar-events" class="mb-3">
                <div class="calendar-events" data-class="bg-info">
                  <i class="fas fa-circle text-info"></i> My Event One
                </div>
                <div class="calendar-events" data-class="bg-success">
                  <i class="fas fa-circle text-success"></i> My Event Two
                </div>
                <div class="calendar-events" data-class="bg-danger">
                  <i class="fas fa-circle text-danger"></i> My Event Three
                </div>
                <div class="calendar-events" data-class="bg-warning">
                  <i class="fas fa-circle text-warning"></i> My Event Four
                </div>
              </div>
              <div class="checkbox mb-3">
                <input id="drop-remove" type="checkbox" class="me-1" />
                <label for="drop-remove"> Remove after drop </label>
              </div>
              <a href="javascript:;" data-bs-toggle="modal" data-bs-target="#add_new_event"
                class="btn mb-0 btn-primary btn-block w-100">
                <i class="fas fa-plus me-1"></i> Add Category
              </a>
            </div>
          </div>
        </div>
        <div class="col-lg-9 col-md-8">
          <div class="card bg-white">
            <div class="card-body">
              <div id="calendar"></div>
              <FullCalendar :options="calendarOptions" :events="events" id="calendar-book"></FullCalendar>
            </div>
          </div>
        </div>
      </div>

      <!-- Add Event Modal -->
      <div id="add_event" class="modal custom-modal fade" role="dialog">
        <div class="modal-dialog modal-dialog-centered modal-md" role="document">
          <div class="modal-content">
            <div class="modal-header border-0 pb-0">
              <div class="form-header modal-header-title text-start mb-0">
                <h4 class="mb-0">Add Event</h4>
              </div>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
                <span class="align-center" aria-hidden="true">×</span>
              </button>
            </div>
            <div class="modal-body">
              <form>
                <div class="input-block mb-3">
                  <label>Event Name <span class="text-danger">*</span></label>
                  <input class="form-control" type="text" />
                </div>
                <div class="input-block mb-3">
                  <label>Event Date <span class="text-danger">*</span></label>
                  <div class="cal-icon">
                    <date-picker v-model="startdate" class="datetimepicker form-control" :editable="true"
                      :clearable="false" :input-format="dateFormat" />
                  </div>
                </div>
                <div class="submit-section">
                  <button class="btn btn-primary submit-btn">Submit</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <!-- /Add Event Modal -->

      <!-- Add Category Modal -->
      <div class="modal custom-modal fade" id="add_new_event">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header border-0 pb-0">
              <div class="form-header modal-header-title text-start mb-0">
                <h4 class="mb-0">Add Category</h4>
              </div>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
                <span class="align-center" aria-hidden="true">×</span>
              </button>
            </div>

            <div class="modal-body">
              <form>
                <div class="input-block mb-3">
                  <label>Category Name</label>
                  <input class="form-control form-white" placeholder="Enter name" type="text" />
                </div>
                <div class="input-block mb-0">
                  <label>Choose Category Color</label>
                  <vue-select :options="Category" id="category-select" placeholder="Choose a color..." />
                </div>
                <div class="submit-section">
                  <button type="button" class="btn btn-primary save-category submit-btn" data-dismiss="modal">
                    Save
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <!-- /Add Category Modal -->
    </div>
  </div>
</template>

<script>
import FullCalendar from "@fullcalendar/vue3";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import interactionPlugin from "@fullcalendar/interaction";
import { ref } from "vue";
const currentDate = ref(new Date());
export default {
  components: {
    FullCalendar,
  },
  props: {
    events: Array,
  },
  data() {
    return {
      startdate: currentDate,
      dateFormat: "dd-MM-yyyy",
      Category: ["Success", "Danger", "Info", "Primary", "Warning", "Inverse"],
      calendarOptions: {
        plugins: [
          dayGridPlugin,
          timeGridPlugin,
          interactionPlugin, // needed for dateClick
        ],
        headerToolbar: {
          left: "prev next today",
          center: "title",
          right: "dayGridMonth,timeGridWeek,timeGridDay",
        },
        events: [
          {
            title: "9:42a Test Event 1",
            start: "2023-10-24",
          },
          {
            title: "7:35a Test Event 3",
            start: "2023-10-26",
          },
          {
            title: "Event Name 4 2:49a",
            start: "2023-10-26",
          },
          {
            title: "Test Event 2 8:22a",
            start: "2023-10-28",
          },
        ],
        initialView: "dayGridMonth",
        editable: true,
        selectable: true,
        selectMirror: true,
        dayMaxEvents: true,
        weekends: true,
      },
    };
  },
};
</script>
